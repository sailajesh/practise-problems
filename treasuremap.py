line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("enter the position: ") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row
letter = position[0].lower()
# print(letter)
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
print(letter_index)
number_index = int(position[1]) - 1
print(number_index)
map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
