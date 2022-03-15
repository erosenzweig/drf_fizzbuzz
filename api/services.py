"""
Services - every non-trivial operation touching the db should be done in a service (update/delete/create).
* Useful for separating business logic from serializer for view responsibility
* Lends itself to unit testing
* Allows reuse of core business logic 
* handles permissions and filtering
"""

from api.models import FizzBuzz

def create_fizzbuzz(*, useragent: str, message: str) -> FizzBuzz:
    fizzbuzz = FizzBuzz(useragent=useragent, message=message)
    fizzbuzz.full_clean()
    fizzbuzz.save()

    return fizzbuzz
