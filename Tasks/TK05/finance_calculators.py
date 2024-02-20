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
