from datetime import datetime
import time


# Part 1
def clock(n):
    '''
    shows the current time
    Parameters
    ----------
    n: int
        number of seconds to show the current time
    '''
    for i in range(n):
        print(str(datetime.today())[11:19], end="\r")
        time.sleep(1)
    #datetime strftime


# Part 2
def lcm(a, b):
    '''
    find the lowest common multiple of a and b
    Parameter
    ----------
    a: int
        number
    b: int
        number

    Returns
    -------
    int
        lowest common multiple of a and b
    '''
    a_original = a
    b_original = b
    while True:
        if a == b:
            return a
        else:
            if a < b:
                a += a_original
            else:
                b += b_original


# Part 3
def gcf(a, b):
    '''
    find the greatest common factor of a and b
    Parameter
    ----------
    a: int
        number
    b: int
        number

    Returns
    -------
    int
        greatest common factor of a and b
    '''
    while True:
        if b == 0:
            return a
        else:
            r = a % b
            a = b
            b = r
