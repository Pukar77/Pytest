#fixtures in pytest are used to prepare things that are needed in test
#in our example, we require my_result in both test functions, so insted of declaring  it in both function, we created a fixture that can be used in both test cases, hence reducing the line of code
 
import pytest
from source import classbasetest
import time

@pytest.fixture
def my_result():
    return classbasetest.Rectangle(10,20)

def test_area(my_result):
    assert my_result.area() == 200
     
def test_perimeter(my_result):
    assert my_result.perimeter() == 60
    
@pytest.mark.slow
def test_perimeter1(my_result):
    time.sleep(5)
    assert my_result.perimeter() == 60
    
@pytest.mark.skip(reason="This feature is currently on work")
def test_skip(my_result):
    assert my_result.perimeter() == 30