import pytest
import fonctions as f

def test_puissances_positives():
    assert f.puissance(2, 3) == 8
    assert f.puissance(2, 2) == 4

def test_puissances_negatives():
    assert f.puissance(-1, 2) == 1
    assert f.puissance(-1, 3) == -1
    assert f.puissance(-2, -1) == -0.5

def test_cas_limites():
    assert f.puissance(0, 5) == 0
    with pytest.raises(ValueError):
        f.puissance(0, -3)

def test_types_invalides():
    with pytest.raises(TypeError):
        f.puissance(2.5, 3)
    with pytest.raises(TypeError):
        f.puissance(2, "3")
