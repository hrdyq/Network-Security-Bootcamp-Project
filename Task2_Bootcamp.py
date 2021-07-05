import hashlib
StringInput = input("Enter any string : ")
OutputA=hashlib.md5(StringInput.encode())
OutputB=hashlib.sha1(StringInput.encode())
OutputC=hashlib.sha224(StringInput.encode())

print("the MD5 Hash of the string {} is {}".format(StringInput, OutputA.hexdigest()))
print("the SHA-1 of the string {} is {}".format(StringInput, OutputB.hexdigest()))
print("the SHA-224 of the string {} is {}".format(StringInput, OutputC.hexdigest()))
