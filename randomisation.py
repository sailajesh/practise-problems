import random
"""by using the seed we will maintain the reproductibility"""
# random.seed(1)
for i in range(10):
    if i<9:
        random_integer = random.randint(1, 15)
        print(random_integer)
"""to get the float number"""
random_float=random.random()
print(random_float)

"""heads or tails"""
# Heads=1
# Tails=0
choice=input("choose 'Heads' or 'Tails' ")
random_choice=random.randint(0,1)
print(random_choice)
if random_choice==1:
    print("Heads")
else:
    print("Tails")
