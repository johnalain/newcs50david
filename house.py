name = input("whats your name : ")
# if name == "Harry" or name == "ron" or name == "bor":
#     print("gryffinder")
# # elif name == "ron":
# #     print("gryffinder")
# # elif name == "bor":
# #     print("gryffinder")
# elif name == "drace":
#     print("Elyffinder")
# else:
#     print("who ?")
#match keyword
match name:
    case "harry" | "hermione" | "ron":
        print("gryffindor")
        # | = or logical operator
        
    # case "hermione":
    #     print("gryffindor")
    # case "ron":
    #     print("gryffindor")
    case "draco":
        print("stytherin")
    case _:
        print("who ?")
    



