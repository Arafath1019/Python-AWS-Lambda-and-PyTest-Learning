import pytest

# @pytest.fixture(params=["a", "b"])
# def demo_fixture(request):
#     print(request.param)
    
# def testLogin(demo_fixture):
#     print("Login Successful")

@pytest.mark.parametrize("a, b, final", [(2, 6, 10), (4, 8, 12), (6, 10, 16)])
def testAdd(a,b,final):
    assert a+b == final