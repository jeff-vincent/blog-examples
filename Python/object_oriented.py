# This is a simple Python class called Person
# Each Person created will have a height and a weight
# Each Person will be able to diet and exercise to lose weight
# Each Person will also be able to feast

class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight
    
    def diet(self):
        self.weight -= 5
    
    def exercise(self):
        self.weight -= 10
    
    def feast(self):
        self.weight += 5


if __name__ == "__main__":
    Tom = Person(170, 250) # Instantiates a new object of the class Person, called Tom
    Carl = Person(180, 70) # Instantiates a new object of the class Person, called Carl
    
    
    print(f"Tom's weight {Tom.get_weight()}")
    print('Tom needs to lose weight, so he diets...')
    
    Tom.diet()
    print(f"Tom's new weight {Tom.get_weight()}")
   
    print('Tom needs to lose more weight, so he exercises...')
    Tom.exercise()
    print(f"Tom's new weight {Tom.get_weight()}")
    print("Great work, Tom!")
    
    print("But then Tom got hungry, so he ate...")
    Tom.feast()
    
    print(f"Tom's new weight {Tom.get_weight()}")
    print(f"Tom {Tom.__dict__}")
    print(f"Carl {Carl.__dict__}")
    

    

    

