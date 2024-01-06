import random
from hangman_words import word_list
from hangman_stages import stages,logo
# names=["sailajesh","jack","pineapple","orange","cherry","frank"]
rand_name=random.choice(word_list)
end_of_game = False
lives = 6
print(logo)
print(f'Pssst, the solution is {rand_name}.')
blank=[]
for i in rand_name:
    i="_"
    blank+=i
# print(blank)

len_name=len(rand_name)
end_of_game=False
while not end_of_game:
    guess = input("guess the letter to fill blank: ").lower()
    if guess in blank:
        print(f"You've already guessed {guess}")
    for position in range(len_name):
        letter=rand_name[position]
        if letter==guess:
            blank[position]=letter
            print(blank)
    if "_" not in blank:
        end_of_game=True
        print("you won")
        # Check if user is wrong.
    if guess not in rand_name:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

        # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(blank)}")

    # Check if user has got all letters.
    if "_" not in blank:
        end_of_game = True
        print("You win.")

    print(stages[lives])



