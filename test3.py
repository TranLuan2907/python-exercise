# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
# (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def calculate_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return ((40 - hours) * 1,5 * rate) + (rate * 40)
    
def check_valid_input(hours, rate):
    while True:
        try:
            hours = float(input("Enter Hours: "))
            rate = float(input("Enter Rate: "))
            return hours, rate
        except ValueError:
            print("Invalid Input!Please enter a number!")
    

hours, rate = check_valid_input()
print("Pay:", calculate_pay(hours, rate))
        