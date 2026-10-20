#for loop or while loop?
#Whilst number is not equal to 1 continue loop - while number != 1
#Begin with positive int
#Rule1: even, divide by 2
#Rule2: odd, multiply 3 and add 1 
#Output to be the number of steps until final number is 1 not the amount


def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    steps_count = 0
    
    while number != 1:  
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
        steps_count += 1
    return steps_count
  
