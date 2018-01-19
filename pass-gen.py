#!/usr/bin/python3

import random
import string

chars = input("Number of chars in password? ")

password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(int(chars))])

print("password: ", password)