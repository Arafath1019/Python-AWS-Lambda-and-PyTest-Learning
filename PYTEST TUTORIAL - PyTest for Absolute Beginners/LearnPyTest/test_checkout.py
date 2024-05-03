import pytest

@pytest.fixture()
def setUp():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("Close Browser")

def testLogin(setUp):
    print("Login Successful")
    
def testLogoff(setUp):
    print("Logoff Successful")

def testCalculation():
    assert 2+2 == 6