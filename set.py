# Creating sets
fruits = {"banana", "orange", "mango", "lemon"}
print(len(fruits))

# We use loops to access items
fruits = {"banana", "orange", "mango", "lemon"}
does_exist = "mango" in fruits
print(does_exist)

# Adding Items to a Set
fruits = {"banana", "orange", "mango", "lemon"}
fruits.add("lime")
print(fruits)

# Adding multiple items using Update()
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
fruits.update(vegetables)
print(fruits)

# Removing items using remove()/pop()
fruits = {"banana", "orange", "mango", "lemon"}
fruits.pop()
print(fruits)

# Clearing Items in a Set using clear()
fruits = {"banana", "orange", "mango", "lemon"}
fruits.clear()
print(fruits)

# Deleting Set using del
fruits = {"banana", "orange", "mango", "lemon"}
del fruits

# Converting List to Set
fruits = ["banana", "orange", "mango", "lemon", "apple", "strawberry"]
fruits = set(fruits)
print(fruits)

# Joining Sets
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
# joining using union()
print(fruits.union(vegetables))

# joinig using update()
fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage", "onion", "carrot"}
fruits.update(vegetables)
print(fruits)

# Finding Intersection Items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.intersection(dragon))

# Checking Subset() and SuperSet()
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))
print(whole_numbers.issuperset(even_numbers))


python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.issubset(dragon))
print(python.issuperset(dragon))

# Checking the Difference() Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers))

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.difference(dragon))    # the result is unordered (characteristic of sets)
print(dragon.difference(python))

# Finding Symmetric Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers))

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.symmetric_difference(dragon))

# Joining Sets
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}
print(python.isdisjoint(dragon))    # False, there are common items

