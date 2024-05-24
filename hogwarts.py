#https://youtu.be/nLRL_NcnK-4?t=12083
#-------list----
# students = ["hermione","harry","ron"]
# print(students[0])
# print(students[1])
# print(students[2])
#------instead u can use loop---
# for student in students:
#     print(student)
#--------list iteration-------
#https://youtu.be/nLRL_NcnK-4?t=12340
# students = ["hermione","harry","ron"]
# for i in range(len(students)):
#     print(i + 1, students[i])

# for i in [0, 1, 2]:#u can use in range(3) instead of [0,1,]]
#     print("Student")
#-----dictionnary-----
#https://youtu.be/nLRL_NcnK-4?t=12738
# students = ["hermione","harry","ron"]
# houses = ["gryffindor", "gryffindor", "gryffindor", "slytherin"]
# students = {"hermione":"gryffindor", "harry":"gryffindor", "ron":"gryffindor","draco": "slytherin"}

# print(students["hermione"])
# print(students["harry"])
# print(students["ron"])
# print(students["draco"])
# for student in students:
#     print(student)#print only the key
#     print(student, students[student], sep = ",")#print the key and value with ,seperator
#----create a dictionary inside list ----
students = [
    {"name": "John", "house": "gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "gryffindor", "patronus": "otte"},
    {"name": "ritan", "house": "salhieh", "patronus": "any"},
    {"name": "ron", "house": "gryffindor", "patronus":"grace little area"},
    {"name": "draco", "house": "stlythinter", "patronus":"None"},#None represent the absent of the value
]
for student in students:
    print(student["name"],student["house"],student["patronus"],sep = " ,")







