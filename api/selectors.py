"""
Selectors - every non-trivial operating fetching data from the database should be done in a selector.
* Useful for separating business logic from serializer for view responsibility
* Lends itself to unit testing
* Allows reuse of core business logic 
* handles permissions and filtering
"""

from typing import Iterable
from api.models import FizzBuzz

def get_fizzbuzz_by_id(*, fizzbuzz_id: int) -> FizzBuzz:
    return FizzBuzz.objects.get(pk=fizzbuzz_id)

def get_fizzbuzzes() -> Iterable[FizzBuzz]:    
    return FizzBuzz.objects.all()
