import pytest
from hamcrest import equal_to, assert_that

class TestSample():
    def test_something(self, first_steps, second_steps):
        first_steps.create_stuff()
        second_steps.verify_stuff()
