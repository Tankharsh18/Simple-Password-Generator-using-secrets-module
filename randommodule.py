#from random import choice
from secrets import choice
import string

#num = ["1","2","3","4","5","6","7","8","9","0"]
#num = "1234567890!@#$%^&*()qwertyuioplkjhgfdsazxcvbnm:`+-*/"

num = string.ascii_letters + string.digits + string.punctuation
password = ""
length =  int(input("How much length need to generate password = "))


for i in range(length):
    password += choice(num)
print(password)
