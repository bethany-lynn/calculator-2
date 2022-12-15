"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
#tokens = input_string.split(' ')   # => ['pow', '3', '5']
#index 0 needs to call the function to get an exponent 
#index 1 will be the coefficient 
#index 2 will be the exponent 
# if statement to call specific power function
#set up a loop that will repeat forever
    #ask for user input
    # if token q, quit loop
    # if ____ (operation), then perform the operation by pulling in the 
    # information needed from the indexing

# A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
    # result = None

while True:
    calculation = input("Please compute: ")
    tokens = calculation.split(' ')
    num1 = float(tokens[1])
    num2 = float(tokens[2])
    result = None

    # if tokens[0] == "q":
    if "q" in tokens:
        break

    else:
        if tokens[0] == "pow":
            result = power(num1, num2)
        elif tokens[0] == "+":
            result = add(num1, num2)
        elif tokens[0] == "-":
            result = subtract(num1, num2)
        elif tokens[0] == "/":
            result = divide(num1, num2)
        elif tokens[0] == "*":
            result = multiply(num1, num2)
        elif tokens[0] == "square":
            result = square(num1, num2)
        elif tokens[0] == "cube":
            result = cube(num1, num2)
        elif tokens[0] == "%":
            result = mod(num1, num2)
        print(result)

        


# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)