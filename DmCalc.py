def factorial(number, factorial_index):
    if number == 0 :
        return 1
    elif number <= factorial_index:
        return number
    else:
        return number * factorial(number - factorial_index, factorial_index)

def Circular_permutation(number):
    try:
        if number > 0 :
            return str(factorial(number - 1, 1))
        else :
            return "Error the number must be a possetive number"
    except  TypeError :
        return "Error the inputs must be integer !"



def Permutation(number1 , number2):
    try:
        if number2 > number1 :
            return "Error, Maybe you wrote the order of the numbers wrong"
        else :
            a = factorial(number1, 1)
            b = factorial(number1 - number2, 1)
            return str(int(a/b))
    except  TypeError :
        return "Error the inputs must be integer !"

def Combination (number1 , number2):
    try:
        if number2 > number1 :
            return "Error, Maybe you wrote the order of the numbers wrong"
        else :
            a = factorial(number1, 1)
            b = factorial(number1 - number2, 1)
            c = factorial(number2, 1)
            return str(int(a/(b*c)))
    except  TypeError :
        return "Error the inputs must be integer !"

def Factorial_operator(cmd):
    try:
        factorial_index = cmd.count("!")
        number = int(cmd.split("!")[0])

        if factorial_index >= number:
            return "Error: factorial index cannot exceed the number"
        else:
            ans = factorial(number, factorial_index)
            return str(ans)
    except  :
        return "Error something went wrong !"

# print(Factorial_operator("10!!!"))