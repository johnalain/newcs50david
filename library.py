#https://youtu.be/nLRL_NcnK-4?t=17555
#-------library python---
#---random docs links ---
#https://docs.python.org/3/library/random.html
# import random
# from random import choice #i cam inport the function choice specificly
# coin = random.choice(["head","tail"])
# coin =choice(["heads", "tail"])# when import the choice function alone i can change coin =choice(["head","tail"]
# a = 2
# b = 10
# num1 = random.randint(a, b)
# # randint(a, b) is a funcion random numbers between a .. b inclusive
# print(coin)
# print(num1)
#----randint(a, b) is a funcion random numbers between---
# import random
# number = random.randint(1, 10)
# print(number)
#----random.shuffle(x) is a funcion --- 
# import random
# cards = ["jack","queen","king"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
# print(cards)
#-----statistics library --------
#https://youtu.be/nLRL_NcnK-4?t=18532
#https://docs.python.org/3/library/statistics.html
# import statistics
# print(statistics.mean([100, 90]))#mean is a function inside statistics  module return average
#---comman-line arguments-----
#https://youtu.be/nLRL_NcnK-4?t=18661
# running file "python3 +file.name"
#------sys---
#https://docs.python.org/3/library/sys.html
# sys.argv (stand for argument vector)
# import sys

# print("hello, my name is", sys.argv[1])# run file "python3 library.py michel" output hello, my name is michel

#------------------
# print("hello, my name is", sys.argv[0])
#python3 library.py run this output the name offile hello, my name is library.py
#------fix index error if u don't mention argv---
# import sys
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("too many arguments")
# ============
# import sys
# #check for errors
# if len(sys.argv) < 2:
#     print("too few arguments")
# elif len(sys.argv)>2:
#     print("too many arguments")

# # print name tags
# print("hello, my name is", sys.argv[1])

#-------sys.exit() function in sys module---
#https://youtu.be/nLRL_NcnK-4?t=19653
# import sys
# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# elif len(sys.argv)>2:
#     sys.exit("too many arguments")
# print("hello, my name is", sys.argv[1])
#-------------------------
# import sys

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# for arg in sys.argv:
#     print("hello my name is", arg)
    # output for command python3 library.py michel rita josephin
# hello my name is library.py
# hello my name is michel
# hello my name is rita
# hello my name is josephin
#----------------------------------
#-------slices--------
#https://youtu.be/nLRL_NcnK-4?t=19963
# import sys

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# for arg in sys.argv[1:]:
#     print("hello my name is", arg)
#-------packages------
#https://youtu.be/nLRL_NcnK-4?t=20192
#-------pypi package-------pypi.org-----
# cowsay is package of python allows
#pypi.org/project/cowsay
#------pip-------
# pip is a program come with python allows you to install packages
# ------install cowsay--pip3 install cowsay--
# import cowsay
# import sys

# # if len(sys.argv) == 2:
# #     cowsay.cow("hello ," +sys.argv[1])
# if len(sys.argv) == 2:
#     cowsay.trex("hello ," +sys.argv[1])
#------API'S----
#---requests packages------
#https://youtu.be/nLRL_NcnK-4?t=20712
#the request library allows to make requests "pip3 install requests"
#pypi.org/project/requests
#https://youtu.be/nLRL_NcnK-4?t=20957











