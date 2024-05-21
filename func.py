# def mik(to ):
#     print("hello,", to)
# name = input("whats ur name: ")
# mik(name) 
# print('--------')
#https://youtu.be/nLRL_NcnK-4?t=5713
# def mike(to = "world"):
#     print("hello,", to)
def main():

    name = input("whats ur name: ")
    return name
    mike()#function is called before u declared but inside main function u can call it like this
   
#https://youtu.be/nLRL_NcnK-4?t=5962
def mike():#u can call the function before u declared but inside another funcntion
    name=name
    print("hello,", name)
main()
#https://youtu.be/nLRL_NcnK-4?t=6229
def main():

    name = input("whats ur name: ")

    mike()
def mike(to = "world"):#u can call the function before u declared but inside another function
    print("hello,", to)
main()
