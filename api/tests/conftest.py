import pytest
from rest_framework.test import APIClient
from api.selectors import get_fizzbuzz_by_id
from api.models import FizzBuzz

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def fizzbuzz_data():
    return [
        {"message": "test_message1"},
        {"message": "test_message2"},
        {"message": "test_message3"},
        {"message": "test_message4"}
    ]

@pytest.fixture
def single_valid_fizzbuzz():
    return {
        "message": "single_fizzbuzz"
    }

@pytest.fixture
def single_invalid_fizzbuzz():
    return {
        "msg": 1234
    }

@pytest.fixture
def create_fizzbuzz(fizzbuzz_data):
    FizzBuzz.objects.bulk_create([ FizzBuzz(useragent="AnonymousUser", message=fb["message"]) for fb in fizzbuzz_data])