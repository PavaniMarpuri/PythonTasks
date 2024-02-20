# read the time taken to complete each event separately

swimming_time = int(input("Please enter the time in minutes taken to complete the Swimming "))
cycling_time = int(input("Please enter the time in minutes taken to complete the Cycling "))
running_time = int(input("Please enter the time in minutes taken to complete the Running "))

# Calculate the total time taken to complete the all three events and printing the total time

triathlon_time = swimming_time + cycling_time + running_time
print(f"Total time taken to complete the triathlon is {triathlon_time}")

if triathlon_time <= 100:
    print("You have completed the events within the qualifying time. You got Provincial Colours award")
elif 101 <= triathlon_time <= 105:  # triathlon_time >= 101 and triathlon_time <= 105
    print("You have completed the events within 5 minutes of the qualifying time. You got Provincial Half Colours "
          "award")
elif 106 <= triathlon_time <= 110:  # triathlon_time >= 106 and triathlon_time <= 110
    print("You have completed the events within 10 minutes of the qualifying time. You got Provincial Scroll award")
else:
    print("You took more than 10 minutes of the qualifying time.So you got No award")
