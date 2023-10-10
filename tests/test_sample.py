import pytest
from hamcrest import equal_to, assert_that

class TestSample():
    def test_something(self):
        assert_that(1, equal_to(1))
