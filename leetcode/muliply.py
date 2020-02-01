# Multiply two numbers by using recursion
def mul(num, n):
    if num > 0:
        return mul(num-1, n) + n
    else:
        return 0

"""This two functions handle even nagitive numbers"""
def mul(num, constant):
    if num < 0:
        return (mul(num+1, constant)) + constant
        
    elif num > 0:
        return mul(num-1, constant) + constant
        
    else:
        return 0


def getNum(num, const):
    if num < 0:
        return -mul(num, const)
    else:
        return mul(num, const)
# getNum(2, 2)

"""This function below solves it without even having another function"""
def mul(num, constant):
    if num < 0:
        # Converting the constant to neg if num is less than 0
        return (mul(num+1, constant)) + (-constant)
        
    elif num > 0:
        return mul(num-1, constant) + constant
        
    else:
        return 0
# mul(2, 2)

"""I just reordered the condition statement from the function right above"""
def mul(num, constant):
    if num == 0:
        return 0
        
    elif num < 0:
        return (mul(num+1, constant)) + (-constant)
        
    else:
        return mul(num-1, constant) + constant
mul(-3, 3)