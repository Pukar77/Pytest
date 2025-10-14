import pytest
from source import classbasetest

@pytest.mark.parametrize('actual_area, expected_area', [(2,4), (3,9), (4,16)])
def test_area(actual_area, expected_area):
    sq = classbasetest.Square(actual_area)
    assert sq.area() == expected_area



