from animals_and_food import *

# Instantiate the Animals
dog = Dog()
cat = Cat()
chick = Chicken()

# Instantiate the Food
lemon = Lemons()
dog_food = DogFood()
cat_food = CatFood()
human_food = HumanFood()
milk = Milk()


# List of Foods as classes and instance objects
foods_as_classes = [Lemons, DogFood, CatFood, HumanFood, Milk, Chicken]
foods_as_instance = [lemon, dog_food, cat_food, human_food, milk, chick]

# List of Animals
animals = [dog, cat]



# Animals Eating
# The animals can be fed either the class itself, or an instance
for animal in animals:
    for food in foods_as_instance:
        animal.eat(food)

    print("\n")

    # # Uncomment this to test the food as classes
    # for food in foods_as_classes:
    #     animal.eat(food)

    # print("\n")

