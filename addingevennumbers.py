value=int(input("enter any number b/w 10 and 100: "))
count=0
for i in range(1,value+1):
    if i%2==0:
        count+=i
print(count)