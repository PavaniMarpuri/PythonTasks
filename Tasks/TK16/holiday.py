"""
This program is to calculate a user’s total holiday cost,
which includes the plane cost, hotel cost, and car-rental cost

Task:-

● Create a Python file called holiday.py.
● Your task will be to calculate a user’s total holiday cost, which includes the
plane cost, hotel cost, and car-rental cost.
● First, get the following user inputs:
        ○ city_flight: The city they will be flying to. (You can create some
        options for them. Remember each city will have different flight
        costs.)
        ○ num_nights: The number of nights they will be staying at a hotel
        ○ rental_days: The number of days for which they will be hiring a
        car.
● Next, create the following four functions:
● hotel_cost: This function will take num_nights as an argument,
and return a total cost for the hotel stay (you can choose the price
per night charged at the hotel).
● plane_cost: This function will take city_flight as an argument
and return a cost for the flight. (Hint: use if/else if statements in
the function to retrieve a price based on the chosen city.)
● car_rental: This function will take rental_days as an argument
and return the total cost of the car rental (you can choose the daily
rental cost.)
● holiday_cost: This function will take the three arguments
hotel_cost, plane_cost, car_rental. Using these three
arguments, you can call all three of the above functions with
respective arguments and finally return a total cost for your
holiday.
● Print out all the details about the holiday in a readable way.
● Try running your program with different combinations of input to show
its compatibility with different options.

"""

"""
function : city_check function will validate city name is valid or not 
whether it is null or value is in mentioned cities
parameter: string
output : boolean
"""


def city_check(city_name):
    if (city_name == " " or city_name is None or city_name.upper() not in
            ("OXFORD", "LONDON", "BRIGHTON", "BELFAST", "LEEDS", "EDINBURGH")):
        return True
    else:
        return False


"""
function : get_user_inputs function will take 3 different inputs and validate their values
whether it is null or value is in required format
parameter: no input parameters
output : three integer values
"""


def get_user_inputs():
    try:
        num_people = int(input("Please enter total no.of people you are planing to go for an holiday "))
    except ValueError as e:
        print(f"Please check your input and enter the correct value. Error: {e}")
        num_people = int(input("Please enter total no.of people you are planing to go for an holiday "))
    try:
        num_nights = int(input("Please enter no.of nights you are staying at the hotel "))
    except ValueError as e:
        print(f"Please check your input and enter the correct value. Error: {e}")
        num_nights = int(input("Please enter no.of nights you are staying at the hotel "))
    try:
        rental_days = int(input("Please enter no.of days you are hiring a car "))
    except ValueError as e:
        print(f"Please check your input and enter the correct value. Error: {e}")
        rental_days = int(input("Please enter no.of days you are hiring a car "))

    return num_people, num_nights, rental_days


"""
function : hotel_cost function will calculate the total hotel cost for the given days
parameter: integer no.of night staying in the hotel
output :  integer value total cost for the given no.of nights
"""


def hotel_cost(nights):
    cost_per_night = 100
    return round(cost_per_night * nights)


"""
function : plane_cost function will return the plan cost for given city
parameter: string city name 
output :  integer value the cost of the plan with respective to the city
"""


def plane_cost(city):
    if city == "OXFORD":
        return 500
    elif city == "LONDON":
        return 800
    elif city == "BRIGHTON":
        return 400
    elif city == "BELFAST":
        return 550
    elif city == "LEEDS":
        return 450
    else:
        return 700


"""
function : car_rental function will calculate the total car rental cost for no.of days
parameter: integer no.of days 
output :  integer value the rental cost for the car for the given no.of days
"""


def car_rental(days):
    cost_per_day = 250
    return round(cost_per_day * days)


"""
function : calculate_cost function will calculate all 3 types of costs 
            including all plan cost, rental cost and hotel cost
parameter: 4 integer values
output :  4 integer values 
"""


def calculate_cost(people, city, nights, days):
    stay_cost, car_cost, flight_cost, total_cost = 0, 0, 0, 0

    if nights is not None:
        stay_cost = hotel_cost(nights)
    if days is not None:
        car_cost = car_rental(days)
    if people is not None:
        flight_cost = plane_cost(city.upper()) * people
    if stay_cost is not None and car_cost is not None and flight_cost is not None:
        total_cost = holiday_cost(flight_cost, stay_cost, car_cost)
    return flight_cost, stay_cost, car_cost, total_cost


"""
function : holiday_cost function will calculate the total holiday cost 
            including all plan cost, rental cost and hotel cost
parameter: 3 integer values
output :  integer value total holiday cost
"""


def holiday_cost(plan_cost, night_cost, car_rent):
    return round(plan_cost + night_cost + car_rent)


"""
main function is the first function that will get invoke 
and calling all the other functions and display the total cost 
and the detailed message to the user
"""


def main():
    city_flight = " "
    # Asking user to enter city name
    while city_check(city_flight):
        city_flight = input("Please enter the city from below list that you are travelling\n"
                            "   Oxford\n"
                            "   Brighton\n"
                            "   London\n"
                            "   Belfast\n"
                            "   Leeds\n"
                            "   Edinburgh ")

    # Invoking the get_user_inputs function to get required details from user
    no_of_people, hotel_nights, car_rental_days = get_user_inputs()

    # Invoking calculate_cost function to calculate plan, hotel, car and total expenditures
    plan_charge, hotel_charge, rental_charges, total_expenditures = (
        calculate_cost(no_of_people, city_flight, hotel_nights, car_rental_days))
    
    # Printing all the details in the console to the user
    print(f"Your Flight charges for {no_of_people} people to the {city_flight} city is {plan_charge}\n"
          f"Your hotel charges for {hotel_nights} nights is {hotel_charge}\n"
          f"Your car rental charges for {car_rental_days} days is {rental_charges}\n"
          f"Your Total expenditures for your holiday is {total_expenditures}\n")


"""
this is the starting point of the program to invoke main function
"""

if __name__ == "__main__":
    main()
