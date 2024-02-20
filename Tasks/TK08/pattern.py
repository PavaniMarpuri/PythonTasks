# importing the math library to use ceil
import math
# user input for total no.of rows of pattern user want
number_of_rows = int(input("Please enter number of rows for the * pattern "))
# Dividing the user entered number by 2 to get the half of the row count value
middle_row_count = math.ceil(number_of_rows / 2)
# declaring a variable to decrement the count when row number reaches more than the half of its value.
decrement_count = 2
# iterating for loop based on row count using range function
for n in range(1, number_of_rows + 1):
    # multiply the count with "*" till the row count reaches half of its value
    # And print the result
    if n <= middle_row_count:
        print(n * "*")
    else:
        # decrement the count by 2 for each iteration when the row count reaches greater than half of its value
        # And multiply the count with "*" .
        # print the result
        print((n - decrement_count) * "*")
        decrement_count += 2
