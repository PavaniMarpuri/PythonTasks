"""
Task:-

● Create a new Python file in this folder called conversion.py
● Please first provide pseudo code as
comments in your Python file, outlining how you will solve this problem.
● Declare the following variables:
○ num1 = 99.23
○ num2 = 23
○ num3 = 150
○ string1 = “100”
● Convert them as follows:
○ num1 into an integer
○ num2 into a float
○ num3 into a String
○ string1 into an integer
● Print out all the variables on separate lines
"""

"""
First declare the given variables
Since num1 is already an integer , no need to convert it
convert num2 as float using float function
convert num3 as String using str function
convert string_var as integer using int function
Finally use print and format functions to print them all separately.
"""

num1 = 99.23
num2 = 23
num3 = 150
string_var = 100

num2 = float(num2)
num3 = str(num3)
string_var = int(string_var)

print(f"num1 {num1}")
print(f"num2 {num2}")
print(f"num3 {num3}")
print(f"string_var {string_var}")


