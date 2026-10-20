"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """returns the exchanged money by dividing the budget by the exchange rate"""
    return budget / exchange_rate

    print(exchange_money(127.5,1.2))


def get_change(budget, exchanging_value):
    """returns the change (remainder) from budget and exchanging value"""
    return budget - exchanging_value
    
    print(get_change(127.5,120))


def get_value_of_bills(denomination, number_of_bills):
    """returns the value of the bills"""
    return denomination * number_of_bills
    
    print(get_value_of_bills(5,125))


def get_number_of_bills(amount, denomination):
    return amount // denomination
    """returns the number of bills that sums the amount """
    print(get_number_of_bills(127.5,5))
    


def get_leftover_of_bills(amount, denomination):
    """Returns how much the booth gets to keep"""
    return amount % denomination
    print(get_leftover_of_bills(127.5,20))
  

def exchangeable_value(budget, exchange_rate, spread, denomination):
    x = exchange_rate * (1 + spread / 100)
    y = budget / x
    return int(y // denomination * denomination)
    """returns the maximum value of the new currency after calculating the exchange rate + the spread"""
    
    print(exchangeable_value(127.25, 1,20, 10, 20))
    

