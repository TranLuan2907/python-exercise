# Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.


def is_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False


def check_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "done":
            return 'done'
        
        if not is_float(user_input):
            print("Invalid Input! Please enter a number!")
        else:
            return float(user_input)


def calculate_sum(number):
    count = len(number)
    total = sum(number)
    if count > 0:
        average = total / count
        print(average)
        print(total)
        print(count)
    else:
        print("No number was entered!")


numbers = []
while True:
    number = check_valid_input("Please enter a number or 'done' to terminate: ")
    if number == 'done':
        break
    numbers.append(number)
    
calculate_sum(numbers)

    

# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.


def is_float2(input):
    try:
        float(input)
        return True
    except ValueError:
        return False
    

def check_valid_input2(prompt):
    while True:
        user_input = input(prompt)
        if user_input == 'done':
                return 'done'
            
        if not is_float2(user_input):
            print("Invalid Input! Plese enter a number!")
        else:
            return float(user_input)


def find_max_min(numbers):
    count = len(numbers)
    if count > 0:
        max_num = max(numbers)
        min_num = min(numbers)
        print(max_num)
        print(min_num)
        print(count)
    else:
        print("No number was entered!")    


numbers = []
while True:
    number = check_valid_input2("Please enter a number or 'done' to terminate: ")
    if number == 'done':
        break
    numbers.append(number)
    
find_max_min(numbers)
    


