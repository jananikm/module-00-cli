import math

def my_abs(y):
    try:
        if y < 0:
            return -y
        else:
            return y
    except TypeError:
        return math.nan