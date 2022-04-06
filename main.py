#Given the below class:
# Create a Class Cat with attributes species, name and age

class Cat: 
  species = 'mammal'

  def __init__(self, name, age, *color):
    self.name = name
    self.age = age
    self.color = color


# 1 Instantiate the Cat object with 3 cats
# Create 3 cats:
mia = Cat('Mia', 4)
john = Cat('John', 5)
sushi = Cat('Sushi', 2)


# 2 Create a function that finds the oldest cat
# create a funtion to find the oldest cat

def get_oldest_cat(*args):
  cat_dict = {}
  for cat in args: 
    cat_dict[cat.name] = cat.age
  oldest = max(cat_dict, key=cat_dict.get)
  print(f'The oldest cat is {oldest} who is {cat_dict[oldest]} years old')

    

  


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

get_oldest_cat(mia, john, sushi)