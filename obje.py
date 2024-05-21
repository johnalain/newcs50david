# test = 'a'
# print(dir(test))
# print all methods belong to this class object
#https://youtu.be/mDKM-JtUhhc?list=PLlvFEn0NKwXIJl9IpuPSWTutoyC0KqXV0&t=29109
# def test():
#     pass
# a = test #i can assign function to this variable
# print(dir(a))#same output as print(dir(test))
# a.another_attribute = 10
#print objects of this function belong to this class one is call 
def add(a, b):
    return a + b
class Test:
    def __init__(self,add_function):
        self.add_function = add_function
test = Test(add_function= add)
print(test.add_function(1, 2))
#https://youtu.be/mDKM-JtUhhc?list=PLlvFEn0NKwXIJl9IpuPSWTutoyC0KqXV0&t=29230
class Monster:
    def __init__(self, func):
        self.func=func
class Attacks:
    def bite(self):
        print(" bite")
        
    def strike(self):
        print(" strike")
    def slash(self):
        print("slash")
    def kick (self):
        print("kick")
attacks = Attacks()
monster = Monster(func = attacks.bite)
monster.func()
#----classes and scope ------------------------
#https://youtu.be/mDKM-JtUhhc?list=PLlvFEn0NKwXIJl9IpuPSWTutoyC0KqXV0&t=29608



