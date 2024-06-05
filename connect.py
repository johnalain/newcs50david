#https://youtu.be/7fSHTqM8gHs?list=PLlvFEn0NKwXJR0BVo-YPTxa8CpIRrI1kZ&t=82
# def connect():
#     raise NotImplementedError('connect()is missing code')
# connect()
# def get_users():
#     users: dict[int, str] = {1: 'bob', 2: 'jef', 3: 'tom'}
#     return users
# print(get_users())
#https://youtu.be/7fSHTqM8gHs?list=PLlvFEn0NKwXJR0BVo-YPTxa8CpIRrI1kZ&t=163
# import random
# random.randint()
# def get_users()-> dict[int,str]:
#     """
#     retrieve the ids and usernames from a database as a dict.
#     :return:dict[int,str]
#     """
#     users: dict[int, str] = {1: 'bob', 2: 'jef', 3: 'tom'}
#     return users
# def display_users(users: dict[int, str])-> None:
#     """
#     prints each user to the console in a nice format
#     :params users:
#     :return:
#     """
#     for k, v in users.items():
#         print(k , v , sep=': ')
# def main() -> None:
#     users: dict[int, str] = get_users()
#     display_users(users)

# if __name__ == '__main__':
#     main()
#https://youtu.be/7fSHTqM8gHs?list=PLlvFEn0NKwXJR0BVo-YPTxa8CpIRrI1kZ&t=440
#--------------------------------------------------------------------

#https://youtu.be/7fSHTqM8gHs?list=PLlvFEn0NKwXJR0BVo-YPTxa8CpIRrI1kZ&t=615
# from enum import Enum
 
# class Quality(Enum):
#     LOW: int = 480
#     MEDIUM: int = 1080
#     HIGH: int = 1440
# class Privacy(Enum):
#     PRIVATE:str = 'private'
#     UNLISTED:str = 'unlisted'
#     PUBLIC:str = 'public'
# def upload(file:str,quality:Quality,privacy:Privacy)->None:
#     print(f'uploading:"{file}" in {quality.value}p ({privacy.value})')

# def main():
#     upload('cat.mp4', Quality.LOW, Privacy.PRIVATE)

# if __name__ == '__main__':
#     main()
#https://youtu.be/7fSHTqM8gHs?list=PLlvFEn0NKwXJR0BVo-YPTxa8CpIRrI1kZ&t=756
def join_text(text1:str,text2:str,text3:str,*,sep:str)->None:
    return sep.join([text1,text2,text3])
def main()->None:
    print (join_text('A', 'B', 'C', sep='-'))
if __name__ == '__main__':
    main()







# print(get_users())

