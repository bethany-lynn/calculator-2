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

while True:
    calculation = input("Please compute: ")
    tokens = calculation.split(' ')



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