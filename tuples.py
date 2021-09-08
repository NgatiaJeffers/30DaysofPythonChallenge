# Creating a Tuple
fruits = ("banana", "orange", "mango", "lemon")
print(len(fruits))

# Accessing a Tuple
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(first_fruit)
print(second_fruit)
print(last_fruit)

# Slicing Tuples
fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_mango = fruits[1:3]
orange_to_the_rest = fruits[1:]
print(all_fruits)
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)

# Negative Indexes
fruits = ("banana", "orange", "mango", "lemon")
all_fruits = fruits[-4:]
orange_mango = fruits[-3:-1]
orange_to_the_rest = fruits[-3:]
print(all_fruits)
print(orange_mango)
print(orange_to_the_rest)

# Changing Tuples to LIsts
fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)
fruits = tuple(fruits)
print(fruits)

# Checking an Item in a List
fruits = ("banana", "orange", "mango", "lemon")
print("orange" in fruits)
print("apple" in fruits)

# Joining Tuples
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Delete Tuples
fruits = ("banana", "orange", "mango", "lemon")
del fruits



