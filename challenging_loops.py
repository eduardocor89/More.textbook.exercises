# Larger Sum
# create a function named larger_sum() that takes two lists
# of numbers as parameters named lst1 and lst2. 
# The function should return the list whose elements sum
# to the greater number. If the sum of the elements
# of each list are equal, return lst1
print("Larger Sum")
def larger_sum(lst1, lst2):
  lst1_total = 0
  lst2_total = 0
  for a in lst1:
    lst1_total += a 
  for b in lst2:
    lst2_total += b 
  if lst1_total > lst2_total:
    return lst1
  elif lst2_total > lst1_total:
    return lst2
  else:
    return lst1 


print(larger_sum([1, 9, 5], [2, 3, 10]))


# Over 9000
# Create a function named over_nine_thousand() that takes a list
# of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum
# is greater than 9000. When this happens, the function should return
# the sum. If the sum of all the elements is never greater than 9000, 
# the function should return total sum of all the elements. If empty, 
# the function should return 0. 
print("\nOver Nine Thousand")
def over_nine_thousand(lst):
  sum = 0 
  if len(lst) == 0:
    return 0
  else:
    for i in lst:
      sum += i 
      if sum >= 9000:
        break
    return sum

print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([]))

print("\nMaximum Number")
# Max Num
# Create a function named max_num() that takes a list
# of numbers named nums as a parameter. 
# The function should return the largest number in nums.


def max_num(nums):
  maximum = nums[0]
  for num in nums:
    if num > maximum:
      maximum = num
  return maximum

print(max_num([50, -10, 0, 75, 20]))
print(max_num([50]))

# Same Values
# Write a function named same_values() that takes two lists
# of numbers equal size as parameters. 
# The function should return a list of the indices where the values
# were equal in lst1 and lst2
print("\nSame Values")
def same_values(lst1,lst2):
  same_values = [x for x in range(len(lst1)) if lst1[x] == lst2[x]]
  return same_values

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# note: Another way of solving this would be the following

def same_values1(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

print(same_values1([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Reversed list
# Create a function named reversed_list() that takes two lists of the
# same size as parameters named lst1 and lst2
# The function should return True if lst1 is the same as lest2 reversed
# The function should return False otherwise.
print("\nReversed List")
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))


