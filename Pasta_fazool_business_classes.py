
'''
We just started an italian restaurant and we need to keep things organized. 
Let's create a menu class where we can keep track of names, items, start_times and end_times.
Create your first Menu by creating a Brunch object, then do the same for an early_bird dinner. 
Do the same with the dinner menu, as well as the kids menu.

Add a __repr__ constructor so that when we use print() on a class object we get something
other than the memory address. 

Add a calculate_bill() method with the parameter purchased_items and have it return the total 
price of the items added to purchased_items.

Let's create a Franchise!

Create a Franchise class and in the constructor, take in an address, and menus.
Create two franchises: the flagship_store and the new_installment stores at any address.
Give the Franchise a string representation method so that we'll be able to tell them apart.
If we use print(franchise) it should tell us the address.

Let's tell our customers what they can order. Give Franchise an available_memnus() method
that takes in time as a parameter and retunrs a list of the Menu objects that are available at that time.

Let's create a business!

Create a business class and in its constructor, a name and a list of franchises.
Our name? "Cho King" best panasian food ever.

Also, make an Arepa place. Before we can make a franchise, we'll need our menu and the time of availability.
Make an arepas_menu, and then arepas_place. You can give it an address when making your Franchise object.

Take away: I created a system of classes that help structure code and perform
all of the business requirements I needed. If I need a new feature, I'll have a good
foundation of organized code to continue developing. 
'''


# As parameters for the Menu class, include name, items, start_time, end_time
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      print("You had a " + item + " that costs $" + 
      str(self.items[item]))
      total += self.items[item]
    return "Your total is $" + str(total)


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = [brunch, early_bird, dinner, kids]
  
  arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
    }

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    for menu in self.menus:
      if time < menu.start_time:
        print( menu.name + " menu not available. Come back at "+ str(menu.start_time))
      elif time >= menu.start_time and time < menu.end_time:
        print(menu.name + " menu available")
      else:
        print("Sorry, " + menu.name + " menu is not available")
    return

class Business:
  def __init__(self, name, franchises):
    self.name = "Basta Fazoolin' with my Heart"
    self.franchises = [flagship_store, new_installment]

  def __repr__(self):
    return self.name 


brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 
'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)

early_bird = Menu("Early-bird Dinner", {'salumeria plate': 8.00, 
'salad and breadsticks (serves 2, no refills)': 14.00, 
'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 15, 18)

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 
'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 
'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00,
 'espresso': 3.00,},17, 23)

kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
'apple juice': 3.00}, 11, 21)


print(kids)
print()
print(brunch.calculate_bill(['tea','tea','coffee']))
print()
print(brunch.calculate_bill(['pancakes','home fries','coffee']))
print()
print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))
print()

#flagship_store = Franchise('1232 West End Road ', menus='')
flagship_store = Franchise('1232 West End Road ','brunch, early bird, dinner and kids menus')
new_installment = Franchise('12 East Mulberry Street ', 'brunch, early bird, dinner and kids menus')
#new_installment = Franchise('12 East Mulberry Street ', menus='')
print(flagship_store)
print(new_installment)
print()
print("Our flagship store:")
print()
print("...if I came in at 12h")
flagship_store.available_menus(12)
print("...if I came in at 17h")
flagship_store.available_menus(17)
print()
# flagship_store.available_menus(0)
# print("...if I came in at -2")
# flagship_store.available_menus(-2)

### Arepa Business
arepa_place = Franchise('189 Fitzgerald Avenue', {'arepa pabellon': 7.00, 
'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50})
#print(arepa_place.arepas_menu)

first_business = Business("Take a' Arepa", arepa_place)
print(first_business)
