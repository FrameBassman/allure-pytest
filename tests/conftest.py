import pytest

from tests.first_steps import FirstSteps
from tests.second_steps import SecondSteps


@pytest.fixture(scope="session")
def first_steps() -> FirstSteps:
    return FirstSteps()

@pytest.fixture(scope="session")
def second_steps() -> SecondSteps:
    return SecondSteps()
