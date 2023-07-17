# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def calculate_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return ((hours - 40) * 1.5 * rate) + (rate * 40)
    
def check_valid_input():
    while True:
        try:
            hours = float(input("Enter Hours: "))
            rate = float(input("Enter Rate: "))
            return hours, rate
        except ValueError:
            print("Invalid Input!Please enter a number!")
    

hours, rate = check_valid_input()
print("Pay:", calculate_pay(hours, rate))


# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score4.14. EXERCISES 55
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly to test the various different values for input.

error = "Bad score"

def computegrade(score):
    if (score < 0 or score > 1):
        return error
    elif (score >= 0.9):
        return "A"
    elif (score >= 0.8):
        return "B"
    elif (score >= 0.7):
        return "C"
    elif (score >= 0.6):
        return "D"
    else:
        return "F"

def check_valid_input():
    while True:
        try:
            score = float(input())
            return score
        except ValueError:
            print(error)
            
score = check_valid_input()
print(computegrade(score))