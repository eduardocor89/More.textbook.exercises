
# Create a list called toppings that holds the following
toppings = ["pepperonoi","pineapple","cheese","sausage","olives","anchovies","mushrooms"]

# Create a list called prices to keep track of how much each costs
prices = [2,6,1,3,2,7,2]

# Count the number of occurrences of 2 in the "prices" list,
# store the result in varible called num_two_dollar_slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# find the length of the toppings and store it in a variable
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# Create a new two dimensional list and store the name and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"] ]
print(pizza_and_prices)
print()
# Sort your new list
pizza_and_prices.sort()
# find the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
# a man walks into the pizza store and shouts "I will have your
# most expensive pizza". Give it to him!
priciest_pizza = pizza_and_prices[-1]
# That was the last slice! Take it off the menu
pizza_and_prices.pop()
# Insert a new peppers pizza that costs 2.5
pizza_and_prices.insert(0,[2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)
# Three mice waslk into the store. They don't have much money
# (they're mice), and each wants a different pizza. Offer them
# the cheapest slices
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

# The mice are very pleased!


