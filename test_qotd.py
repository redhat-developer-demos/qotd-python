import pytest
from qotd import getQuoteById

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")

def test1():
    print("Executing test1!")
    assert True

def test2():
    print("Executing step 2")
    assert True

def test_getQuoteById():
    assert getQuoteById(1) == "foo"

    