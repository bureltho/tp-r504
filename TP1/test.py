import pytest
import fonctions as f

def test_1():
		assert f.puissance(2,3) == 8
		assert f.puissance(2,2) == 4
def test_2():

    assert f.puissance(-1, 1) == -1
    assert f.puissance(-1, 2) == 1
    assert f.puissance(-2, 1) == -2
    assert f.puissance(-2, 3) == -8
    
    assert f.puissance(-12, 1) == -12
    assert f.puissance(-13, 1) == -13
    assert f.puissance(-1, -1) == -1
    assert f.puissance(-1, -2) == 1
