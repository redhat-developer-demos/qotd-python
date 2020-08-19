import pytest

@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")

@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nSetup Class2")

@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetup Function2")

class TestClass:
    def test_it(self):
        print("TestIt")
        assert True
    
    def test_it2(self):
        print("TestIt2")
        assert True