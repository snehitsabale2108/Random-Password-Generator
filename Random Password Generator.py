import random
import string

s = string.ascii_letters+string.digits+string.punctuation
print(s)
n = int(input("Enter the Length of Passwd: "))

passwd = "".join(random.choice(s) for i in range(n))
print("Your Passwd is: ", passwd)
