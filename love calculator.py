print("the love calculator is calculating the score.")
name1=input("enter your name ").upper()
name2=input("enter your name ").upper()
count1=0
count2=0
x='TRUE'
y='LOVE'
for i in name1:
    if i in x :
        count1+=1
for w in name2 :
    if w in x:
        count1+=1
for l in name1:
    if l in y :
        count2+=1
for g in name2 :
    if g in y:
        count2+=1
comb=str(count1)+str(count2)
score=int(comb)
print(score)
if score < 10 or score>90:
    print(f"your score is {score} you two together like coke and mentos")
elif 40<=score<=50:
    print(f"your score is {score},you are alright together")
else:
    print(f"your score is {score},normal")