import random
import string 

chars = string.digits + string.ascii_letters

name = input("Enter your Fist_last name: ").split()
lenght = int(input("Enter your charactors lenght: "))
name = ''.join(name)
print('*******************************')
print('Here are your User Name: ')
for pwd in range(1):
    user_name = ""
    for ch in range(lenght):
        user_name += random.choice(chars)
    print(name+user_name)
print('*******************************')
