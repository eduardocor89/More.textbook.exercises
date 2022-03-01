
# Ground shipping
weight = 0
cost = 0

print("For regular ground shipping")
if weight <= 2:
  cost = weight * 1.50 + 20
  #print("Your cost is $1.50 per pound")
  print("Total: $" + str(cost))
elif weight > 2 and weight <= 6:
  cost = weight * 3.00 + 20
  #print("Your cost is $3.00 per pound")
  print("Total: $" + str(cost))
elif weight > 6 and weight <= 10:
  cost = weight * 4.00 + 20
  #print("Your cost is $4.00 per pound")
  print("Total: $" + str(cost))
else:
  cost = weight * 4.75 + 20
  #print("Your cost is $4.75 per pound")
  print("Total: $" + str(cost))

# Premium Ground
premium_ground_cost = 125
print("\nFor Premium Ground Shipping your cost is $" + str(premium_ground_cost) + "\n")


# Drone Shipping
drone_weight = 0
drone_cost = 0
print("With Drone shipping: ")
if drone_weight <= 2:
  drone_cost = drone_weight * 4.50
  print("Your total is $" + str(drone_cost))
elif drone_weight > 2 and drone_weight <= 6:
  drone_cost = drone_weight * 9
  print("Your total is $" + str(drone_cost))
elif drone_weight > 6 and drone_weight <= 10:
  drone_cost = drone_weight * 12
  print("Your total is $" + str(drone_cost))
else:
  drone_cost = drone_weight * 14.25
  print("Your total is $" + str(drone_cost))

print("\n\nFor a package that's 4.8 lbs it is cheaper by regular ground at $34.4 vs $125 and $43.19")

print("For a package that's 41.5 lbs it is cheaper by premium ground at $125 vs $217.12 and $591.37")

