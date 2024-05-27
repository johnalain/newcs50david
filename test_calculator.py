# #https://youtu.be/nLRL_NcnK-4?t=22432
# from calculator import square
# def main():
#     test_square ()
# def test_square():
#     try:    #--------assert--------
#         assert square(2) == 5
#     except:print ("4 was not  square  2")
#     try:
#         assert square(3) == 9
#     except:print ("3 was not  square  9")
#     try:
#         assert square(-2) == 4
#     except:print ("-2 was not  square 4 ")
#     try:
#         assert square(-3) == 9
#     except:print ("9 was not  square  -3")

#     try:
#         assert square(0) == 0
#     except:print ("0 was not square  0")
   

    

    # if square(2)!=4:
    #     print("2 squared is not 4")
    # if square(3) !=9:
    #     print("3 squared is not 9")
# if __name__ == "__main__":
#     main()
    #AssertionError car when import square from other file calculator.py i put n + n instead of square n * n

 #----pytest-----https://youtu.be/nLRL_NcnK-4?t=23191--
    # ---you should download and install pytest-----
    # --you dont have to write many lines to test your code---
from calculator import square
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    #--run pytest <file name> command output

# ========================== FAILURES ===========================
# _________________________ test_square _________________________

#     def test_square():
#         assert square(2) == 4
# >       assert square(3) == 9
# E       assert 6 == 9
# E        +  where 6 = square(3)

# test_calculator.py:40: AssertionError
# =================== short test summary info ===================
# FAILED test_calculator.py::test_square - assert 6 == 9
# ====================== 1 failed in 0.24s ======================
# ====================== 1 failed in 0.24s ======================
# michelkadi@mss-MacBook javascript22hours % pytest test_calculator.py
# =================================================== test session starts ===================================================
# platform darwin -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0
# rootdir: /Users/michelkadi/javascript22hours
# collected 1 item                                                                                                          

# test_calculator.py .                                                                                                [100%]

# ==================================================== 1 passed in 0.03s ====================================================
# michelkadi@mss-MacBook javascript22hours % 
   
#     #pip3 install pytest



