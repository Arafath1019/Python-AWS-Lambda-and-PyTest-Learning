import pytest

# @pytest.fixture(autouse=True, scope="session")
# def setUp():
#     print("Launch browser")
#     print("Login")
#     print("Browse products")
#     yield
#     print("Close Browser")

@pytest.fixture(scope="session", autouse=True)
def setUp(browser):
    if browser == "chrome":
        print("Launch chrome browser")
    if browser == "firefox":
        print("Launch firefox browser")
    if browser == "edge":
        print("Launch edge browser")
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("Close Browser")
    
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")