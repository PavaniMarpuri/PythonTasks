"""
Task:-

● Create a file called student_register.py
● Write a program that allows a user to register students for an exam venue.
● First, ask the user how many students are registering.
● Create a for loop that runs for that number of students.
● Each time the loop runs the program should ask the user to enter the
next student ID number.
● Write each of the ID numbers to a text file called reg_form.txt
● Include a dotted line after each student ID because this document will be
used as an attendance register, which the students will sign when they
arrive at the exam venue

"""

# creating a variable for file name
file_name = "reg_form.txt"
# Asking user to enter no.of students
student_count = int(input("Please enter no.of students registering for an exam "))
# Displaying a msg to the user to enter the student id in correct format
print("Please enter student ID contains alphanumeric with length of 10 ")
# Error handling with try except when dealing with files
try:
    # opening a file in write mode and assigning file object to local variable called file
    with open(file_name, 'w') as file:
        # writing a header to the file
        file.write(5 * "\t" + "STUDENT REGISTRATION FORM" + 2 * "\n")
        # for loop to iterate for the given number of students
        for i in range(student_count):
            # created a local variable that will be used in future to save student id
            student_id = " "
            # checking if the student is not an alphanumeric or its length  is not 10
            while (not student_id.isalnum()) or (not len(student_id) == 10):
                # and asking user to enter student id
                student_id = input(f"Please enter correct student {i + 1} ID : ")
            # writing the student id to the file followed by dotted line
            file.write(student_id.upper() + "\t" + 20 * "." + "\n")
except FileNotFoundError:
    print(" Please check the file name/ file Path ")
except IOError as e:
    print(" Please enter proper values ")
