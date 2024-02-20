# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")  # SyntaxError: Missing parentheses in call to 'print'
print("\n")  # IndentationError type of syntax error & SyntaxError: Missing parentheses in call to 'print'

# Variables declaring the user's age, casting the str to an int, and printing the result
# age_Str = "24 years old"
age_Str = "24"  # IndentationError type of syntax error & NameError: name 'age_Str' is not defined
age = int(age_Str)  # IndentationError type of syntax error & ValueError: invalid literal for int() with base 10
print("I'm " + str(age) + " years old.")  # IndentationError type of syntax error &
# TypeError: can only concatenate str (not "int") to str

# Variables declaring additional years and printing the total years of age
years_from_now = "3"  # IndentationError type of syntax error
total_years = age + int(years_from_now)  # IndentationError type of syntax error &
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("The total number of years:" + str(total_years))  # SyntaxError: Missing parentheses in call to 'print' &
# and changes the answer_years to total_years without " " to print value

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  # NameError: name 'total' is not defined
print("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old")  # SyntaxError: Missing parentheses in call to 'print' & TypeError: can only concatenate str (not "int") to str
# & added 6 more months as it is 3 years 6 months

# HINT, 330 months is the correct answer
