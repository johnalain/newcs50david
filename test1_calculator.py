from calculator import square
import pytest
def test_positive():
    assert square(2)==4
    assert square (3)==9
def test_negative():
    assert square(-2)==4
    assert square(-3)==9
def test_zero():
    assert square(0)==0
def test_str():
    with pytest.raises(TypeError):
        square("cat")
#michelkadi@mss-MacBook javascript22hours % pytest test1_calculator.py
# michelkadi@mss-MacBook javascript22hours % pytest test1_calculator.py
# =================================================== test session starts ===================================================
# platform darwin -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0
# rootdir: /Users/michelkadi/javascript22hours
# collected 3 items                                                                                                         

# test1_calculator.py ...                                                                                             [100%]

# ==================================================== 3 passed in 0.02s ====================================================
# # michelkadi@mss-MacBook javascript22hours 

# test1_calculator.py ...                                                                                             [100%]

# ==================================================== 3 passed in 0.02s ====================================================
# michelkadi@mss-MacBook javascript22hours % 