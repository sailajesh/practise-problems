import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options=[rock,paper,scissors]
choice=int(input("enter your inputs 0 for rock 1 for paper 2 for scissors: "))
if choice>=3 or choice<0:
    print("you have entered wrong option play again")
else:
    print(options[choice])
    sys_rand=random.randint(0,1)
    print(f"computer choose{sys_rand}")
    print(options[sys_rand])

    if choice==0 and sys_rand==2:
         print("you won")
    elif sys_rand==0 and choice==2:
         print("you lose")
    elif sys_rand>choice:
         print("you lose")
    elif choice>sys_rand:
         print("you won")
    elif choice==sys_rand:
         print("Draw")
    else:
         print("wrong choice")

