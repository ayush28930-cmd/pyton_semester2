# Student Result Calculator

name = input("Enter student name: ")

marks = []
total = 0

for i in range(5):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
    total += mark

average = total / 5

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)