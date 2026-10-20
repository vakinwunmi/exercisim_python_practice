#classify a leap year 
#year % 4 = 0 - this means that it is divisible by 4
#if year % 100 = 0 then year also % 400 = 0 to  be a leap year
#Output needs to be bol as task is to find if year is a leap year - returns true/false

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
 
