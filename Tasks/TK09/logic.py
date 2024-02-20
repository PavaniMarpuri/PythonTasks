"""
program to display star pattern for example like below
*
**
***
****
***
**
*
"""
import math

"""
Approach :- Till half of the row count (count*"*")
            After half count reducing the count by one and multiplying with * .
"""
number_of_rows = int(input("Please enter number of rows for the * pattern "))
middle_row_count = math.ceil(number_of_rows / 2)
decrement_count = 1
for n in range(1, number_of_rows + 1):
    if n <= middle_row_count:
        print(f"{n * "*"}")
    else:
        print(f"{(n - decrement_count) * "*"}")
        decrement_count += 1
