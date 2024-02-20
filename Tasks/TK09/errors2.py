"""
Task:-

● Attempt to run the program. You will encounter various errors.
● Fix the errors and then run the program.
● Each time you fix an error, add a # comment in the line where you fixed it
and indicate which of the three types of errors it was with a brief
explanation of why that is.
● Save the corrected file.

"""

# This example program is meant to demonstrate errors.)
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # NameError: name 'Lion' is not defined
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# in above statement added f to print the values and
# replaced the number_of_teeth and animal_type respectively to print correct values at correct place

print(full_spec) # SyntaxError: Missing parentheses in call to 'print'.

