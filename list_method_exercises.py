# Create a function called append_size() that has one
# parameter named lst. 
# The function should append the size of lst (inclusive)
# to the end of lst. The function should then return this new list

#Write your function here
def append_size(lst):
  to_append = len(lst)
  lst.append(to_append)
  return lst
  

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# Write a function named append_sum that has one parameter — a list named named lst.

# The function should add the last two elements of lst together and append the result to lst. 
# It should do this process three times and then return lst.

def append_sum(lst):
  counter = 0
  while counter <= 2:
    lst.append(lst[-1] + lst[-2])
    counter += 1
     
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# Write a function named larger_list that has two parameters named lst1 and lst2
# The function should return the last element of the list that contains
# more elements. If both lists are the same size, then return the last element
# of list1

#Write your function here
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]


#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

    
