'''to calculte the body mass index'''
height=input("enter the height ")
weight=input("enter the weight ")
a=float(height)
b=int(weight)
bmi=int(b/(a*a))
print(round(bmi,2))
a=float(height)
b=int(weight)
bmi=b/(a*a)
# print(round(bmi,2))
if bmi<18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi>18.5 and bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >=25 and bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>=30 and bmi<35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")