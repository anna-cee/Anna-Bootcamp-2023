#main.py

# import functions
# import sys

# print("And the answer to the equation is….")
# answer = functions.sum(3, 6)
# print(answer)

# print("The paths that Python looks for modules is….")
# print(sys.path)


#main.py
#filepath for namespace

# import stuff.functions


# print("And the answer to the equation is….")
# answer = stuff.functions.sum(3, 6)
# print(answer)


#main.py
#Alias
# import stuff.functions as funky

# print("And the answer to the equation is….")
# answer = funky.sum(3, 6)
# print(answer)

#direct call
#main.py

# from stuff.functions import sum

# print("And the answer to the equation is….")
# answer = sum(3, 6)
# print(answer)

#some examples from standard library

# main.py

# import math

# num1 = math.ceil(2.1)
# num2 = math.floor(2.9)

# print(num1)
# print(num2)


# # main.py

# import random

# num = random.random()

# print(num)


#math and random together

# main.py

# import random
# import math

# random_number = math.ceil(random.random() * 10)

# print(random_number)

#random can pick a random number form a sequence

# main.py

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

random_letter = random.choice(alphabet)

print(random_letter)