#-----Exceptions------
#https://youtu.be/nLRL_NcnK-4?t=14855
#----Try----except----

# try:
#     x = int(input("what is x? "))
    
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")
# #----------------
# while True:
#     try:
#         x = int(input("what is x? : "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")
def main():
   x = get_int()
   print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("what is x? : "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x
main()
#https://youtu.be/nLRL_NcnK-4?t=16748


