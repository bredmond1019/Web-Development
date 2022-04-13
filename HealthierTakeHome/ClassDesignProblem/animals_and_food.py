
# Food Base Class
class Food:
    # Each Subclass should have a class attribute "name"
    name = None

    # Each Subclass will also have an instance name 
    # which should be defaulted to the class attribute of name
    # Ex: salmon, carrots, puppy chow, 2% Milk, etc
    def __init__(self, name = None):
        self.name = name

    # How an Instance of the class will be displayed
    def __repr__(self):
        return f"{self.name}"
    


# Each Food Class Inheritated From Food Base Class
class CatFood(Food):
    name = "cat food"
    
    def __init__(self):
        Food.__init__(self, name = "cat food")


class DogFood(Food):
    name = "dog food"
    
    def __init__(self):
        Food.__init__(self, name = "dog food")


class HumanFood(Food):
    name = "human food"
    
    def __init__(self):
        Food.__init__(self, name = "human food")


class Milk(Food):
    name = "milk"

    def __init__(self):
        Food.__init__(self, name = "milk")


class Lemons(Food):
    name = "lemons"

    def __init__(self):
        Food.__init__(self, name = "lemons")




# Animal Base Class
class Animal:
    def __init__(self, noise = "", foods = []):
        self.noise = noise
        self.liked_foods = foods
    

    def make_noise(self):
        print(self.noise)
    

    def eat(self, meal):
        likes_meal = False
        
        for food in self.liked_foods:
            if meal == food or isinstance(meal, food):
                likes_meal = True
        
        if likes_meal:
            print(f"The {self} liked the {meal.name}")
            for i in range(3):
                self.make_noise()
        else:
            print(f"The {self} didn't like the {meal.name}")
            self.make_noise()


    def __repr__(self):
        return f"{type(self).__name__}"
        


# Animals Inherited from Animal Base Class

# Chicken is both an animal and food so it inherits from both classes
class Chicken(Food, Animal):
    name = "chicken"

    def __init__(self):
        Animal.__init__(self, noise="cluck")
        Food.__init__(self, name = "chicken")

# These two of top of the food chain in this crew of animals, so just inherit from animal
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, noise="bark", foods=[DogFood, CatFood, Chicken, HumanFood])


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, noise="meow", foods=[CatFood, Chicken, Milk])