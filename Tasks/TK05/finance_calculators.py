"""
Task:-

● Create a new Python file in this folder called finance_calculators.py.
● Write the code that will do the following:
1. The user should be allowed to choose which calculation they want to do.
The first output that the user sees when the program runs should look like
this :
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed:
2. How the user capitalises their selection should not affect how the
program proceeds. i.e. ‘Bond’, ‘bond’, ‘BOND’ or ‘investment’, ‘Investment’,
‘INVESTMENT’, etc., should all be recognised as valid entries. If the user
doesn’t type in a valid input, show an appropriate error message.
3. If the user selects ‘investment’, do the following:
● Ask the user to input:
○ The amount of money that they are depositing.
○ The interest rate (as a percentage). Only the number of the interest
rate should be entered — don’t worry about having to deal with the
added ‘%’, e.g. The user should enter 8 and not 8%.
○ The number of years they plan on investing.
○ Then ask the user to input if they want “simple” or “compound”
interest, and store this in a variable called interest. Depending on
whether or not they typed “simple” or “compound”, output the
appropriate amount that they will get back after the given period,
at the specified interest rate. See below for the formula to be used:
Interest formula:
The total amount when simple interest is applied is calculated as
follows:A = P *(1 + r*t)
The total amount when compound interest is applied is calculated as
follows: 𝐴 = 𝑃(1 + 𝑟)
𝑡
The Python equivalent is slightly different: A = P * math.pow((1+r),t)
In the formulae above:
● ‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
then r is 0.08.
● ‘P’ is the amount that the user deposits.
● ‘t’ is the number of years that the money is being invested.
● ‘A’ is the total amount once the interest has been applied.
○ Print out the answer!
○ Try entering 20 years and 8 (%) and see what the difference is
depending on the type of interest rate!
4. If the user selects ‘bond’, do the following:
● Ask the user to input:
○ The present value of the house. e.g. 100000
○ The interest rate. e.g. 7
○ The number of months they plan to take to repay the bond. e.g. 120
Bond repayment formula:
The amount that a person will have to be repaid on a home loan each
month is calculated as follows:
repayment = (i * P)/(1 - (1 + i)**(-n))
In the formula above:
● ‘P’ is the present value of the house.
● ‘i’ is the monthly interest rate, calculated by dividing the annual
interest rate by 12. Remember to divide the interest entered by
the user by 100 e.g. (8 / 100) before dividing by 12.
● ‘n’ is the number of months over which the bond will be repaid.
○ Calculate how much money the user will have to repay each month
and output the answer.
"""

import math

# Take user choice

user_choice = input("""investment - to calculate the amount of \
interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: """)

# Checking if user choice is investment

if user_choice.lower() == "investment":
    # Taking the required inputs from user amount,interest rate, no.of years and type of interest
    try:
        amount = int(input("Please enter the deposit amount "))
        interest_rate = int(input("Please enter interest rate "))
        years = int(input("Please enter the number of years " +
                          "that the money is being invested. "))
        interest_type = input("Please enter the interest type " +
                              "whether 'simple' or 'compound' ")
        # Checking if the interest type is simple interest
        if interest_type.lower() == "simple":
            # Formula for simple interest
            total_amount = amount * (1 + (interest_rate / 100) * years)
            # Print the total interest to be paid for the mentioned no.of years
            print(f"Total Amount you will get after {years} years " +
                  f"for simple interest is {total_amount} ")
        # Checking if the interest type is compound interest
        elif interest_type.lower() == "compound":
            # formula for compound interest
            total_amount = amount * math.pow((1 + (interest_rate / 100)), years)
            # Print the total interest to be paid for the mentioned no.of years
            print(f"Total Amount you will get after {years} years " +
                  f"for compound interest is {total_amount} ")
        # Printing else msg if the user entered wrong input
        else:
            print("Please enter the valid interest type 'Simple/Compound' ")
    except ArithmeticError as a:
        print(f"Arithmetic error occurred {a}")
    except IOError as e:
        print(f"Please enter correct values {e}")
    except Exception:
        print("Exception Occurred ")
# Checking if user choice is bond
elif user_choice.lower() == "bond":
    # Taking the required inputs from user house value,interest rate and  no.of months
    try:
        house_value = int(input("Please enter the present value of the house "))
        interest_rate = int(input("Please enter the interest rate "))
        months = int(input("Please enter the number of months you " +
                           "are plan to take to repay the bond "))
        # Formula for bond interest
        total_amount = (((interest_rate / 12) / 100) * house_value) / (
                1 - (1 + ((interest_rate / 12) / 100)) ** (-months))
        # Print the total interest to be paid for each month
        print(f"The amount that you will have to be repaid " +
              f"on a home loan each month is {total_amount} ")
    except ArithmeticError as a:
        print(f"Arithmetic error occurred {a}")
    except IOError as e:
        print(f"Please enter correct values {e}")
    except Exception:
        print("Exception Occurred ")
else:
    print("Please enter valid choice")
