"""
Task:-
● Create a file called while.py.
● Write a program that continually asks the user to enter a number.
● When the user enters “-1”, the program should stop requesting the user
to enter a number,
● The program must then calculate the average of the numbers entered,
excluding the -1.
● Make use of the while loop repetition structure to implement the
program.

"""
total = 0
count = -1
user_input = 0
# if the number entered by user is not -1 then
# increasing the count and calculating the total of the number
while user_input != -1:
    count += 1
    total += user_input
    user_input = int(input("Please enter a Number "))
average = total / count
print(f"The average of {count} numbers you have entered is {average}")
