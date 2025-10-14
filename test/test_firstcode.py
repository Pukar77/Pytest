import pytest
from source import firstcode 

def test_add():
    result = firstcode.add(2,3)
    assert result == 5


def test_mul():
    result = firstcode.mul(2,3)
    assert result == 6
    
#testing for strings
def test_add_strings():
    result = firstcode.add('hey ', 'pukar')
    assert result == 'hey pukar'