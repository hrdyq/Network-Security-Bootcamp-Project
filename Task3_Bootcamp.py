import hashlib
import string
import random  
S = 5       
password = input("Enter the Password : ")

for i in range(0,5):
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    salt1 = str(ran) + password
    password = salt1

print(password)
hashed=hashlib.md5(password.encode())
print("The Salted Hash is ",hashed.hexdigest())
