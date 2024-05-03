import pytest

def testLogin():
    print("Login Successful")

@pytest.mark.regression
def testLogoff():
    print("Logoff Successful")

@pytest.mark.sanity
def testCalculation():
    assert 2+2 == 6