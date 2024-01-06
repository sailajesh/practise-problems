"""who will pay the bill"""
import random

# names=input("enter the names ")
# names_split=names.split(", ")
# length=len(names_split)
# random_integer = random.randint(0,length-1)
# print(random_integer)
# person=names_split[random_integer]
# print(f"{person} is going to pay the bill")
#
# print(names_split)
import random

names = input("Enter the names: ")
names_split = names.split(", ")
length = len(names_split)
random_integer = random.randint(0, length-1)
person = names_split[random_integer]
print(f"{person} is going to pay the bill")
