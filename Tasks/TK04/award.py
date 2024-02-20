"""
Task:-

● Create a new Python file in this folder called award.py.
● Design a program that determines the award a person competing in a
triathlon will receive.
● Your program should read in the times (in minutes) for all three events of a
triathlon, namely swimming, cycling, and running, and then calculate and
display the total time taken to complete the triathlon.
● The award a participant receives is based on the total time taken to
complete the triathlon. The qualifying time for awards is 100 minutes.
Display the award that the participant will receive based on the following
criteria:

Qualifying Criteria         -    Time Range                     -   Award
-------------------------------------------------------------------------------------------
1.  Within the qualifying time  -    0 - 100 minutes              -   Provincial Colours
2.  Within 5 minutes of the
qualifying time.                -    101 - 105 minutes            -   Provincial Half Colours
3.  Within 10 minutes of the
qualifying time.                -    106 - 110 minutes            -   Provincial Scroll
4.  More than 10 minutes off
from the qualifying time.       -    111+ minutes                 -    No award
----------------------------------------------------------------------------------------------


"""

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
