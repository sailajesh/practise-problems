import math
def paint_calc(height,width):
    number_of_cans=math.ceil((height*width)/(5))
    return number_of_cans
print(paint_calc(7,5))
'''to check prime number or not'''
n=int(input("enter the number"))
for i in range(2,n):
    if n%i==0 and i!=n:
        print("not prime")
        break
else:
    print("prime")