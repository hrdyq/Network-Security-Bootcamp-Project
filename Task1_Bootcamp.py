import hashlib
input1=input("Enter any string : ")
output = hashlib.md5(input1.encode())
print("The MD5 hash of the string {} is {}.".format(input1,output.hexdigest()))


