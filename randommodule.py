from secrets import choice
import string

num = string.ascii_letters + string.digits + string.punctuation
password = ""
length =  int(input("How much length need to generate password = "))

for i in range(length):
    password += choice(num)
print(password)
