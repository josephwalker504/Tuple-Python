# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("tiger", "lion", "monkey", "zebra", "honey badger", "gorilla", "jaguar", "cheetah", "wolves", "egale")

# Find one of your animals using the tuple.index(value) syntax on the tuple.
zoo.index("tiger")
print(zoo.index("honey badger"))

# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "kangaroo"
if animal_to_find in zoo:
    print("Animal was found")

# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# 
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple, and print them to the console.

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, sveenth_animal, eighth_animal, ninth_animal, tenth_animal) = zoo
print(second_animal)
print(tenth_animal)
print(first_animal)

# Convert your tuple into a list

list_to_tuple = list(zoo)
print(list_to_tuple)

# Use extend() to add three more animals to your zoo.
animal_for_list = ("alligator", "elephant", "giraffe")
list_to_tuple.extend(animal_for_list)
print(list_to_tuple)

# Convert the list back into a tuple.

def convert(list_to_tuple):
    return tuple(list_to_tuple)

print(list_to_tuple)