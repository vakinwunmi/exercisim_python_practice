# Work out how many digits number has 
# Raise each digit to that number and add together
# The sum of the numbers equals the og number
 
def is_armstrong_number(number):
    digits = str(number) #loops through each digit
    power = len(digits) #finds the number of digits to raise
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number
