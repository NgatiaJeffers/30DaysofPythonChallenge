# syntax
lst = list()

empty_list = list() # empty list, no item in the list
print(len(empty_list))

# syntax
lst = []

empty_list = [] # this is an empty list, no item in the list
print(len(empty_list))

# List with initial values. We use len() to find the length of a list
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yoghurt"]
web_techs = ["HTML", "CSS", "JS", "React", "Redux", "Node", "Mongo"]
countries = ["Finland", "Estonia", "Denmark", "Sweden", "Norway"]

# Print the list and its length
print("Fruits:", fruits)
print("Number of fruits:", len(fruits))
print("Vegetables:", vegetables)
print("Number of vegetables:", len(vegetables))
print("Animal Products:", animal_products)
print("NUmber of animal products:", len(animal_products))
print("web technologies:", web_techs)
print("Number of web technologies:", len(web_techs))
print("Countries:", countries)
print("Number pf countries:", len(countries))

# List having different data types
lst = ["Jefferson", 230, True, {"Country":"Kenya", "city":"Nairobi"}]

# Accessing List Items
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

# Unpacking List Items
lst = ["item", "item2", "item3", "item4", "item5"]
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

# First Example
fruits = ["banana", "orange", "mango", "lemon"]
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

# Second Example
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

# Thirs Example
countries = ["Kenya", "Hawaii", "Sweden", "Finland", "Norway", "Iceland", "Estonia", "Denmark"]
kn, hw, sw, fn, *scandic, nr = countries
print(kn)
print(hw)
print(sw)
print(fn)
print(scandic)
print(nr)

# Slicing Items from a List
# positive indexing
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:]
print(all_fruits)
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2]
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

# Modifying Lists
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)
fruits[1] = "apple"
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = "lime"
print(fruits)

# Checking Items in a List
fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "lime" in fruits
print(does_exist)

# Adding Items to a List
fruits = ["banana", "orange", "mango", "lemon"]
# append(item)
fruits.append("apple")
print(fruits)
fruits.append("lime")
print(fruits)

# Inserting Items into a List
fruits = ["banana", "orange", "mango", "lemon"]
# insert(index, object)
fruits.insert(2, "apple")
print(fruits)
fruits.insert(3, "lime")

# Removing Items from a List
fruits = ["banana", "orange", "mango", "lemon"]
fruits.remove("banana")
print(fruits)
fruits.remove("lemon")
print(fruits)

# Removing Items Using Pop()
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# Removing Items Using del
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:3] # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)

# Clearing List Items
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
# clear()
fruits.clear()
print(fruits)

# Copying a List
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
fruits_copy = fruits.copy()
print(fruits_copy)

# Joining Lists
# Plus Operator
positive_numbers = [1,2,3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
# Joining using extend() method
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numbers:", num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1,2,3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers:", negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print("Fruits and vegetables:", fruits)

# Counting Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
# count()
print(fruits.count("orange"))
ages = [23, 17, 18, 25, 26, 24, 19, 24, 19, 23, 23]
print(ages.count(19))

# Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
# index()
print(fruits.index("orange"))
ages = [23, 17, 18, 25, 26, 24, 19, 24, 19, 23, 23]
print(ages.index(24)) # returns the index of an item in the list

# Reversing a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print("New fruits Order:", fruits)
ages = [23, 17, 18, 25, 26, 24, 19, 24, 19, 23, 23]
ages.reverse()
print("Age Order:", ages)

# Sorting List Items
fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()   # Sorted in alphabetic order
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [23, 17, 18, 25, 26, 24, 19, 24, 19, 23, 23]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)
# sorted()
fruits = ["banana", "orange", "mango", "lemon"]
print(sorted(fruits))
# Reverse order
fruits = ["banana", "orange", "mango", "lemon"]
fruits = sorted(fruits, reverse=True)
print(fruits)
