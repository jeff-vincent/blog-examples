from person import Person
from pet import Pet
from grocery_store import GroceryStore

# a Pet called fluffy
fluffy = Pet('Fluffy', 100)
fluffy.pet_type = 'dog'

# a Person called Tom
tom = Person('5\'8"', 250, fluffy) 

# a GroceryStore
grocery_store = GroceryStore() 

print(f"Tom weighs {tom.get_weight()} lbs")
print('Tom needs to lose weight, so he diets...')
print('\n')
tom.diet()
print(f"Tom's new weight {tom.get_weight()}")
print('\n')
print('Tom decides to lose more weight, so he exercises...')
tom.exercise()
print(f"Tom's new weight is {tom.get_weight()}")
print("Great work, Tom!")
print('\n')
print("But then Tom got hungry, so he ate...")
tom.feast()
print(f"Tom's new weight is {tom.get_weight()}")
print('\n')
print(f"Later, Tom walks his {tom.pet.pet_type} named {tom.pet.name} to the grocery store")
print('\n')
print(f"The grocery store has the following number of the following items {grocery_store.items}")
print('\n')
print("Tom buys a carton of milk")
grocery_store.sell_item({'name': 'milk', 'count': 1})
print('\n')
print(f"Now the grocery store has the following number of the following items {grocery_store.items}")
