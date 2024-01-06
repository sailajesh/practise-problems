import random
print("welcome to guess number game")
random_num=random.randint(1,100)
print(random_num)
easy=10
hard=5
def game(attempts):
    while attempts>0:
        guess = int(input("guess the number: "))
        if guess<random_num:
            print("Too low")
        elif guess>random_num:
            print("Too high")
        elif guess==random_num:
            print("you have guessed the number")
            break
        attempts=attempts-1
        print(f"you have {attempts} attempts left to guess the number")
    else:
      print(f"you are out of moves the correct answer is {random_num}")

def main():
    choose=input("choose 'easy' or 'hard': ")
    if choose=='easy':
        game(attempts=easy)
    elif choose=='hard':
        game(attempts=hard)
main()






