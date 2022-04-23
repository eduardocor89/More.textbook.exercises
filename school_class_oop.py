""""
Created two classes and defined their interactions. Just a simple example
of object-oriented programming.
"""



# Let's define a student class and add a constructor that'll take in two
# parameters: name and year
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass

    def get_average(self):
      total = 0
      for grade in self.grades:
        total += grade
      return average/len(self.grades)

# Now let's make 3 instances of students
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

###################Test Area############################
roger.add_grade(100)
print(roger.self.grades)



########################################################

# Create a Grade class with minimum_passing grade as an attribute
# and set it to 65. Give it a constructor and assign score to it.


class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score 
  
  def is_passing(self):
    if self.score > self.minimum_passing:
      return "Passing"
    else:
      return "Not Passing"

# Add an add_grade() method to student that takes a parameter grade
# add_grade() should verify that grade is of type Grade and if so add it
# to the student's .grades
# if grade isn't an instance of grade then .add_grade() should do nothing

# Create a new grade with a score of 100 and add it to pieter's .grades 
# using .add_grade()

# Additionally you could:
# Write a Grdae method is_pasing() that returns wether a Grade has a passing score
# Write a Student method get_average() that returns the student's average score

grade = Grade(100)
pieter.add_grade(grade)
grade2 = Grade(64)


