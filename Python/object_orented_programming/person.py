class Person:
    def __init__(self, height, weight, pet=None):
        self.height = height
        self.weight = weight
        self.pet = pet


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
