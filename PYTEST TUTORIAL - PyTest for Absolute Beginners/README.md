## Download & install python
- https://www.python.org/
- check python version: python3 --version
- check pip version: pip3 --version

## Install PyTest
- pip3 install -U pytest
- check pytest version: pytest --version
- Uninstall pytest: pip3 uninstall pytest

## Naming convention for pytest python file
- Starting of filename like "test_*.py" or ending filename like "*_test.py"
- Any method inside the test file will be considered as a test
- Method name for test will be start with "test", for example: testLogin()

## Execute PyTest Tests from Command line
- Run "pytest" command inside project directory
- Run "pytest -v", "pytest -v -s" commands for detail tests
- Run test on specific file: "pytest file_directory"

## Grouping tests in PyTest
- Mark a test case method using the @pytest.mark decorator with a builtin or custom marker, for example: 
```
@pytest.mark.sanity
def testCalculation():
    assert 2+2 == 4
```
- Run a test using marker: pytest -m sanity
- Check list of built in markers: pytest --marker
- skip marker: @pytest.mark.skip
- xfail marker:  @pytest.mark.xfail