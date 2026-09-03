'''
- Create a list of 5 animals called zoo
- delete the animal at 3rd index
- append a new animal at the end of the list
- delete the animal at the beginning of the list 
- print all the animal
- print only the first 3 animal
'''

zoo = ["tiger", "monkey", "lion","monkey, gorilla"]

zoo.pop(3)

zoo.append("lizard")
zoo.pop(0)

print(zoo)

print(zoo[0:3])