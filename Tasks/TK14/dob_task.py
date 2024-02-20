"""
Task:-
● Create a new Python file in the Dropbox folder for this task, and call it
dob_task.py.
● In your Python file, write a program that reads the data from the text file
provided (DOB.txt) and prints it out in two different sections in the format
displayed below:

Name
Orville Wright
Rogelio Holloway
Marjorie Figueroa
… etc.

Birthdate
21 July 1988
13 September 1988
9 October 1988
… etc.

"""

# creating a variable for file name
file_name = "DOB.txt"
# Error handling with try except when dealing with files
try:
    # opening a file in read mode and assigning file object to local variable called file_data
    with open(file_name, 'r') as file_data:
        # using the readlines() method to read all the lines in the file.
        # Which wil return the data in the form of list[strings]
        name_dob_data = file_data.readlines()
        # printing the readlines data
        # print(name_dob_data)
        # splitting the list data based on spaces , which will create a 2D list
        list_data = [x.split(" ") for x in name_dob_data]
        # printing the 2D list data
        # print(list_data)
        # printing the "Name" as heading
        print("\033[1mName \033[0m")
        # iterating over 2D list and printing first two index data as this contains names
        for value in list_data:
            print(value[0], value[1])
        # printing the "Birthdate" as heading
        print("\033[1mBirthdate \033[0m")
        # iterating over 2D list and printing last 3 index data as this contains birthdate
        for value in list_data:
            print(value[2], value[3], value[4].strip("\n"))
except FileNotFoundError:
    print(f"Please check your file")
except IOError as e:
    print(f"Error reading the file : {e}")
