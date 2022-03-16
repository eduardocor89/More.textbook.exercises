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

# Create a function that takes the last two items of a list
# and adds them together. Make it do this three times in total. 
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

def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]


#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


# Create a function named more_than_n that has three parameters named lst, item and n
# The function should return True if the item appears in the list more than n times. 
# The function should return False otherwise

def more_than_n(lst,item, n):
  if lst.count(item) > n:
    return True
  False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


# Write a function named combine_sort that has two parameters
# named lst1 and lst2. 
# The function should combine these two lsits into one new
# list and sort the result. Return the new sorted list. 

def combine_sort(lst1,lst2):
  new_lst = lst1 + lst2
  return sorted(new_lst)

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
