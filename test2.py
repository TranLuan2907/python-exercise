# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

rate = float(input("Enter rate: "))
hours = float(input("Enter hours: "))
extra_hours = max(hours - 40, 0)
extra_pay = 0.5 * rate * extra_hours
pay = rate * hours + extra_pay
print("Pay:", pay)

# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:

error_numeric_input = "Error, please enter numeric input"
try:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    
except ValueError:
    print(error_numeric_input)
    quit()

extra_hours = max(hours - 40, 0)
extra_pay = 0.5 * rate * extra_hours
pay = rate * hours + extra_pay
print("Pay", pay)        

# Exercise 3: Write a program to prompt for a score between 0.0 and
# 1.0. If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade using the following table:3.11. EXERCISES 41
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for
# input.
error = "Bad score"
try:
    score = float(input("Enter score: "))
    if score > 1 or score < 0:
        print(error)
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except ValueError:
        print(error)
           
                

