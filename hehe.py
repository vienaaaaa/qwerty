import random
element = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_password = int(input("Bikin password (gakbakal dihack kok)"))

password = ""
for i in range (panjang_password):
    password += random.choice(element)

print(password)





