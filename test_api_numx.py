import pytest
from numx.Numx import Numx

@pytest.fixture
def numrx():
    # All setup for the Numx ...
    return Numx(5)

def test_check_number(numrx):
    numrx.get_fact()
    assert 5 == 5

