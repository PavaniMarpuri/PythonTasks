"""
Task:-

● Imagine you are running a cafe. Create a new Python file in your folder
called cafe.py.
● Create a list called menu, which should contain at least four items sold in
the cafe.
● Next, create a dictionary called stock, which should contain the stock
value for each item on your menu.
● Create another dictionary called price, which should contain the prices for
each item on your menu.
● Next, calculate the total_stock worth in the cafe. You will need to
remember to loop through the appropriate dictionaries and lists to do
this.
● Finally, print out the result of your calculation.
"""

#  length of the list from user
menu_length = int(input("Please enter total no.of the items sold in the cafe "))
# creating a list by taking the items of the list from the user based on the length of the list
menu = [input(f"Please enter name of the item {i} :- ") for i in range(0, menu_length)]
# printing the menu list
print(f" Your Item List is :- {menu}")
# Declaring an empty dictionary to store item and respective stock values
stock = {}
# Declaring an empty dictionary to store item and respective price values
price = {}
for item in menu:
    # iterating over list and assigning the key as item and asking user to enter stock value
    stock[item] = int(input(f"Please enter stock value of the item {item} "))
    # iterating over list and assigning the key as item and asking user to enter price of the item
    price[item] = int(input(f"Please enter price of the item {item} "))
# printing the item respective stock values
print(f" Your items respective stock is:- {stock}")
# printing the item respective prices
print(f" Your items respective price is:- {price}")
# declaring a variable to store total stock worth in the cafe
total_stock = 0
for item in menu:
    # iterating over the menu list and taking stock value from stock dictionary by passing the item as key
    # And taking price value from price dictionary by passing the item as key
    # finally multiplying both to get total stock worth
    total_stock += stock[item] * price[item]
# printing the total stock worth
print(f" The total stock worth in the cafe is {total_stock}")

