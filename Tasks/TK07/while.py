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
