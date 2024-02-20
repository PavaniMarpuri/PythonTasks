"""
Task:-

● Create a new Python file in the Dropbox folder for this task, and call it
details.py
● Please first provide pseudo code as comments in
your Python file, outlining how you will solve this problem.
● Get the following information from the
user.
○ Name
○ Age
○ House number
○ Street name
● Print out a single sentence containing all the details of the user.
"""

"""
Take all the values one by one using input function and assign to variables respectively
print the sentence as requested using print and format functions.

"""

name = input("Please Enter Name ")
Age = input("Please Enter Age ")
house_number = input("Please Enter House Number ")
street_name = input("Please Enter Street Name ")
print(f"This is {name}. He/She is {Age} years old and lives at house number {house_number} on {street_name} Street.")
