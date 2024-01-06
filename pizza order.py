print("Thank you for choosing the sams pizza")
size=input("choose your size of the pizaa s,m or l ")
add_chicken=input("want chicken Y or N ")
add_cheese =input("want cheese Y or N ")
price=0
if size=='s':
    price=15
elif size=='m':
    price=20
elif size =='l':
    price=25
if size=='s'and add_chicken=='Y':
    price+=2
elif (size == 'm' or size=='l') and add_chicken == 'Y':
    price += 3
if add_cheese=='Y':
    price+=1
print(f"your total price for the pizza {price}")