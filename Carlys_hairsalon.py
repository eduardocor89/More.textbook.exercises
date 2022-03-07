# Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

# First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Loop through the prices list and add each price to the variable total_price.
total_price = 0
for price in prices:
  total_price += price

# After your loop, create a variable called average_price that is the total_price divided by the number of prices.

average_price = total_price/len(prices)
print("Your Average Haircut Price: " + str(average_price))

# That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

# Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

new_prices = [ (price -5 ) for price in prices]
print(new_prices)

# Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

total_revenue_by_cut = []
for i in range(len(hairstyles)):
  total_revenue_by_cut.append(last_week[i] * prices[i])

# Add the product prices and the number of people who got the haircut.
total_revenue = 0
for amount in total_revenue_by_cut:
  total_revenue += amount
print("Your Total Revenue is: " + str(total_revenue))

# Find the average daily revenue 
average_daily_revenue = total_revenue/7
print("Average daily Revenue: "+ str(average_daily_revenue))

# Carly thinks she can bring in more customers y advertising all of the haircuts she has that are under 30 dollars. Make a list that represents this.
cuts_under_30 = [new_prices[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)
