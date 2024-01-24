# 1. Create a list of cafe menu items
menu = ["Toast",
        "Eggs",
        "Beans",
        "Sausages",
        "Tea"
        ]

# 2. Create a dictionary with the stock value of the menu items
stock = {"Toast" : 0.50,
         "Eggs" : 0.20,
         "Beans" : 0.40,
         "Sausages" : 0.50,
         "Tea" : 0.50
         }

# 3. Create a new dictionary with the price per menu item
price = {"Toast" : 0.50,
         "Eggs" : 0.20,
         "Beans" : 0.40,
         "Sausages" : 0.50,
         "Tea" : 1.20
         }

# 4. Make up the total quantity of each stock item 
quantity = {"Toast" : 500,
         "Eggs" : 450,
         "Beans" : 300,
         "Sausages" : 1000,
         "Tea" : 580
        }

"""
5. Calculate the total stock worth by doing the following:

    1. Calculate the item_value (stock * price) for each item on the menu:
        Take the stock price in the stock dictionary
        Muiltiply the stock price by the amount in the price dictionary

    2. Calculate the value of stock available: 
        Multiply the item_value by the quantity of stock in the cafe

"""

# Initialise containers
item_value = ()
total_stock = ()

for i, item in enumerate(stock,1):   
    if item in stock and item in price:
        # Calculate the item value
        item_value = (stock[item] * price[item])
        print(i,(f"The item value for {item} is: £{item_value:.2f}\n"))
        # Calculate the quantity of stock available  
        stock_worth = (stock[item] * price[item] * quantity[item])
        total_stock =+ stock_worth
       

print(f"The total menu stock is worth: £{total_stock:.2f}")
        




