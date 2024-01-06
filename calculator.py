'''calculator '''
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
operations={'+':add,
            '-':sub,
            '*':mult,
            '/':div
            }
def calculator():
    print(logo)
    n1=float(input("enter the number: "))
    for symbol in operations:
        print(symbol)
    while True:
        n2=float(input("enter the number: "))

        select_operation=input("select any above symbol: ")
        function=operations[select_operation]
        result=function(n1,n2)
        print( f"{n1} {select_operation} {n2} = {result}")
        more_cal=input("type y for more calculations or  type 'n' to start a new calculations : ")
        if more_cal=="y":
            n1=result
        else:
            break
    calculator()

calculator()
# select_operation=input("select any above symbol: ")
# n3=int(input("enter the 3number: "))
# '''here we are using the result1  as the one of the parameter'''
# function=operations[select_operation]
# result2=function(result1,n3)
# print( f"{result1} {select_operation} {n3} = {result2}")
