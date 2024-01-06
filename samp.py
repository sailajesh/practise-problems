# message = "the soil says i am alive but there are no one to hear"
# def msg(message):
#     message="water"
#     print(message)
# def msg(message):
#     message="soil" + message
#     print(message)
# msg(message)
# print(message)
# request = "everything was allright"
# a=request[0:-10]
# print(a)
# enter=input("enter the number ")
# a=int(enter[0])
# b=int(enter[1])
# c=a+b
# print(c)
# name="sailajesh"
# a=f"my name is {name},{name}"
# print(a)
# '''check even or odd'''
# number = int(input("enter the number "))
# if number%2==0:
#     print("even number")
# else:
#     print("odd number")
# height=int(input("enter the height"))
# if height >=120:
#     print("eligible for ride")
# age=int(input("enter the age"))
#     # elif age>18
# """leap year"""
# year=int(input("enter the year "))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print("leap year")
# else:
#     print("not leap year")
#
# a='''Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')'''
#
# print(a)
#
# a="hello"
# b="world"
# temp=a
# a=b
# b=temp
# print(a)
# print(b)
#
# def msg():
#     return ("Hello")
# msg()

'''Dictionary problems'''
# a={"name":"sailajesh","age":27,"email":"sailajesh134@gmail.com",
#    "occupation":"software developer"}
# print(a["name"])
#
# s=input("enter the teext: ")
# if any(char.isalnum() for char in s):
#     print("True")
# elif any(char.isalpha() for char in s):
#     print("True")
# elif any(char.isdigit() for char in s):
#     print("True")
# elif any(char.islower() for char in s):
#     print("True")
# elif any(char.isupper() for char in s):
#     print("True")
# else:
#     print("False")

details={"fruits":["mango","apple","watermelon","tomato"],"animals":["lion","dog","cat"]}
travel={"India":{"states_visited":["ap","ts","karnataka","tamilnadu","orissa","pondichery"],"total_cities":8}}
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict["c"]=[1,2,3]
# print(dict[1]=4)
# print(dict)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)


width=int(input("enter number: "))
c="H"
for i in range(1, width + 1):
    line = c * (2 * i - 1)
    print(line.center(width * 2 - 1, ' '))
    # print('H'*width)
