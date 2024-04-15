def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def isThisBranch():
    print("This is a branch")

if __name__ == '__main__':
    result1 = add(5, 5)
    result2 = subtract(5, 3)
    print(result1, result2)
    isThisBranch()