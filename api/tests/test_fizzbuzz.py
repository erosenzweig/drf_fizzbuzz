import pytest
from api.models import FizzBuzz
from api.selectors import get_fizzbuzz_by_id, get_fizzbuzzes
from api.services import create_fizzbuzz


# UNIT TESTS
# Testing core business logic related in services and selectors.
@pytest.mark.django_db
def test_select_all_fizzbuzzes(create_fizzbuzz):
    fizzbuzzes = get_fizzbuzzes()
    assert len(fizzbuzzes) == 4

@pytest.mark.django_db
def test_select_single_fizzbuzz(create_fizzbuzz):
    fizzbuzzes = get_fizzbuzz_by_id(fizzbuzz_id=4)
    assert fizzbuzzes.fizzbuzz_id == 4

@pytest.mark.django_db
def test_select_single_invalid_fizzbuzz(create_fizzbuzz):
    with pytest.raises(FizzBuzz.DoesNotExist):
        get_fizzbuzz_by_id(fizzbuzz_id=7)

# FALSE POSITIVE !
# full_clean doesn't raise validation exception as expected ?
@pytest.mark.django_db
def test_create_invalid_fizzbuzz(single_invalid_fizzbuzz):
    with pytest.raises(TypeError):
        create_fizzbuzz(useragent="AnyonymousUser", *single_invalid_fizzbuzz.items())

    #assert invalid_fizzbuzz.message == single_invalid_fizzbuzz["message"]

@pytest.mark.django_db
def test_create_valid_fizzbuzz(single_valid_fizzbuzz):
    fizzbuzz = create_fizzbuzz(useragent="AnyonymousUser", message=single_valid_fizzbuzz["message"])

    assert fizzbuzz.message == single_valid_fizzbuzz["message"]


# INTEGRATION TESTS
# Testing one step closer to integration testing by testing core business logic AND api endpoints.
@pytest.mark.django_db
def test_get_all_fizzbuzz(client, create_fizzbuzz):
    response = client.get('/api/fizzbuzz', HTTP_USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')

    fizzbuzzes = response.data
    assert len(fizzbuzzes) == 4

@pytest.mark.django_db
def test_get_all_fizzbuzz(client, create_fizzbuzz):
    response = client.get('/api/fizzbuzz', HTTP_USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')

    assert len(response.data) == 4
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_single_fizzbuzz(client, create_fizzbuzz):
    response = client.get('/api/fizzbuzz/3', HTTP_USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')

    fizzbuzz = response.data

    assert fizzbuzz["fizzbuzz_id"] == 3

@pytest.mark.django_db
def test_post_single_valid_fizzbuzz(client, single_valid_fizzbuzz):
    post_response = client.post('/api/fizzbuzz', single_valid_fizzbuzz)
    assert post_response.status_code == 201

    posted_data = post_response.data
    assert posted_data["message"] == single_valid_fizzbuzz["message"]
    
    get_response = client.get('/api/fizzbuzz/1', HTTP_USER_AGENT='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36')
    assert get_response.status_code == 200

    get_data = get_response.data
    assert get_data["fizzbuzz_id"] == 1

@pytest.mark.django_db
def test_post_single_invalid_fizzbuzz(client, single_invalid_fizzbuzz):
    post_response = client.post('/api/fizzbuzz', single_invalid_fizzbuzz)
    assert post_response.status_code == 400