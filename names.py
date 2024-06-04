# names = []
# for _ in range (3):

#     names.append(input("whats your name? "))
# for name in sorted(names):
#     print(f"hello, {name}")
#------open-----
#docs.python.org/3/library/functions.html#open
# name = input("what's your name? ")
# file = open("names.txt", "a")#change "w" to append "a" to avoid overwriting
#https://youtu.be/nLRL_NcnK-4?t=25644
# file.write(f"{name}\n")
# file.close()
#----with ----
# name = input("what's your name? ")
# with open("names.txt", "a")as file:
#     file.write(f"{name}\n")
# file.close()#instead of file.close()we can use with as above
#-----read the file-----
# with open("names.txt", "r")as file:
#     lines = file.readlines()
# for line in lines:
#     print("hell, ",line.rstrip())# use "rstrip" to avoid gap between lines
#https://youtu.be/nLRL_NcnK-4?t=26264
# with open("names.txt", "r")as file:
#     for line in file:
#         print("hello, ",line.rstrip())
#same code as above
#https://youtu.be/nLRL_NcnK-4?t=26460
# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.strip())
# for name in sorted(names):
#     print(f"hello, {name}")
#same as above----

# with open("names.txt") as file:
#     for line in sorted (file):
#         print(f"hello, ", line.rstrip())
        # -------
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())
for name in sorted(names, reverse=True):
    print(f"hello, {name}")
#---read documentation for ascending and descending sort "docs.python.org/3/library/functions.html#sorted"--
#https://youtu.be/ywg7cW0Txs4?list=PLhQjrBD2T380F_inVRXMIHCqLaNUd7bN4 david .malan c language---


