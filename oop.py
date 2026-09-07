class Dog:
    # The constructor to set up data
    def __init__(self, name, breed):
        self.name = name    # Attribute unique to each dog
        self.breed = breed  # Attribute unique to each dog

    # A method (action) the dog can perform
    def bark(self):
        return f"{self.name} says Woof!"

# 2. Create Objects from the Class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Rex", "German Shepherd")

# 3. Access attributes and call methods
print(my_dog.name)       # Output: Buddy
print(your_dog.breed)    # Output: German Shepherd
print(my_dog.bark())     # Output: Buddy says Woof!
print(your_dog.bark())   # Output: Rex says Woof!