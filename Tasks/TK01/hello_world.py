"""
Task:

● Create a new Python file in the Dropbox folder for this task, and call it
hello_world.py.
● First, provide pseudo code as comments in your Python file, outlining
how you will solve this problem (you’ll need to read the rest of this
practical task first of course!).
● Now, inside your hello_world.py file, write Python code to take in a user’s
name and then print out the name.
● Use the same input and output approach to take in a user’s age and
print it out.
● Finally, print the string “Hello World!” on a new line.

"""

"""
take the name from user using input function
print the name using print function
Now inside print function use input function to take age from user.
Note :- Since we are not doing any operation using age ,we are just printing it. So I am not converting it to int.
Now print “Hello World!” using print function
"""

user_name = input("Please enter User Name ")
print("User name is " + user_name)
print("User age is " + str(int(input("Please Enter User age "))))
print("“Hello World!”")
