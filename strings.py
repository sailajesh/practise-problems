# '''change case of the input string'''
# s=input("enter the string: ")
# txt=""
# for char in s:
#     if char.isupper():
#         txt = txt + char.lower()
#     elif char.islower():
#         txt+= char.upper()
#     else:
#         txt+=char
# print(txt)
# '''split and join'''
# def split_and_join(line):
#     # write your code here
#    s=line.split(" ")
#    s="-".join(s)
#    return s
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
# def mutate_string(string, position, character):
# string=input("enter string: ")
# position=int(input("enter number: "))
# character=input("enter the character: ")
# a=string[:position] + character + string[position+1:]
# print(a)
def greet(name,age):
    print(f"hello {name} my age is {age}")
greet(name="sam",age=26)

'''Find the string occurence'''
msg=input("enter the text: ")
letter=input("enter the sub_string want to find: ")
def count_substring(string, sub_string):
    count=0
    for char in string:
        if char==sub_string:
            count=count+1
    return count
print(count_substring(string=msg,sub_string=letter))
