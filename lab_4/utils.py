import math

def factorial_n(num):
    return math.factorial(num)

def prime_number(num):

    # define a flag variable
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

def is_power(x, y):
     
    # The only power of 1
    # is 1 itself
    if x == 1:
        return y == 1
         
    # Repeatedly compute
    # power of x
    pow = 1
    while pow < y:
        pow = pow * x
 
    # Check if power of x
    # becomes y
    return pow == y