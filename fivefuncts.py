#https://youtu.be/CnbgMnUCsUM
# -----function1 exec()---
# text: str ='''
# print ('hello,Bob')
# my_range: range = range(4)
# for i in my_range:
#     print(i)
# print("i'm code being executed")
# print('never used exce()with file you dont trust')
# '''
# exec(text)
# user_input:str = input('write same code: ')
# exec(user_input)
#-------------------------------------------------------
#-----function2 Partial------
# from functools import partial
# def specifications(colour:str, name:str, amount:int)-> None:
#     print(f'specs: {colour}, {name}, {amount=}.')

# specifications("red", "bob",10)
# specifications("red", "bob",5)
# specifications("red", "bob",20)
#---------------------------------

# colour_and_name_specs: partial = partial(specifications, amount=10)
# colour_and_name_specs('red', 'bob')
#-----------------------------------
#https://youtu.be/CnbgMnUCsUM?t=345
# specify_amount: partial = partial(specifications, 'blue', 'bob')
# specify_amount(10)
# specify_amount(5)
# specify_amount(1000)
#-----------------------------------
# specify_name: partial =partial(specifications, 'green',amount=10)
# specify_name('michel')
# specify_name('Amanda')
# specify_name('bob2')
#------------------------------------------------------------function 3------
# from itertools import permutations, combinations_with_replacement
# def main()->None: 
#     perms: permutations[str] = permutations(['A','B','C','D'])
#     # print(tuple(perms))
#     #same as print(tuple(perms))
#     for a, b, c, d in tuple(perms):
#         print(a, b, c, d)

# def main() ->None:
#------------combinations----------------
# def main()->None:
#     type str_combs = combinations_with_replacement[str] 
#     combs: str_combs = combinations_with_replacement(['a', 'b', 'c'],3)
#     print(tuple(combs))
 
# if __name__ == '__main__':
#     main()
#--if you want all possible combinations(wich include repeating elements and different orders check out:
# intertools.product
#https://youtu.be/CnbgMnUCsUM?t=640

#----------------------function 4-------------------------------
#https://youtu.be/CnbgMnUCsUM?t=818
# from random import choice, choices, sample
# names:list[str] = ["georges","michel","rita","josephine"]
# winner:str = choice(names)
# print (winner)
# winners: list[str] =sample(names,k=3)
# print (winners)
# random_names: list[str] = choices(names,k=2)
# print (random_names)
#============================================================
#https://youtu.be/CnbgMnUCsUM?t=1016
from tkinter import filedialog as fd
path: str = fd.askopenfilename(title = 'Select File',initialdir='/Users/michelkadi/Desktop')
print(path)
#to open a file or folder when running
