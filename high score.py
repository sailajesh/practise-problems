"""to find the highest score using for loops"""
student_scores = input("enter the scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for i in student_scores:
    if i > highest_score:
        highest_score=i
print(highest_score)

