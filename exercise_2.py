
# Exercise 2: Grade Categorizer

grade = float(input("Enter the grade:"))

try:
    if grade >= 90 and grade <= 100:
        print("Excellect! You've got A grade.")
    elif grade >= 80 and grade < 90:
        print("Very Good! You've got B grade.")
    elif grade >= 70 and grade < 80:
        print("Good! You've got C grade.")
    elif grade >= 60 and grade < 70:
        print("Average! You've got D grade.")
    else:
        print("You've failed. It is an F.")
except grade != -1 and grade > 100:
    print("Invalid input!!!")