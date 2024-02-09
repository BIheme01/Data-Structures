# 1. Create a list of cafe menu items
menu = ["Toast",
        "Eggs",
        "Beans",
        "Sausages",
        "Tea"
        ]

# 2. Create a dictionary with the stock value of the menu items
# Stock value represents the item quantity
stock = {"Toast" : 500,
         "Eggs" : 450,
         "Beans" : 300,
         "Sausages" : 1000,
         "Tea" : 580
        }

# 3. Create a new dictionary with the price per menu item
price = {"Toast" : 0.50,
         "Eggs" : 0.20,
         "Beans" : 0.40,
         "Sausages" : 0.50,
         "Tea" : 1.20
         }

"""
4. Calculate the total stock worth by doing the following:

    1. Calculate the item_value (stock * price) for each item on the menu.
    2. Sum up the item_value for each menu item.
"""

# Initialise containers
item_value = ()
total_stock_worth = 0

for i, item in enumerate(price,1):   
    if item in price and item in stock:
        # Calculate the item value
        item_value = (stock[item] * price[item])
        print(i,(f"The item value for {item} is: £{item_value:.2f}\n"))
        # Calculate the total stock worth
        total_stock_worth += item_value
       

print(f"The total stock worth is: £{total_stock_worth:.2f}")
        












        




