# Declare a variable

a = 3
b = 2

# Arithmetic operations
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print("a + b = ", total)
print("a - b = ", diff)
print("a * b = ", product)
print("a / b = ", division)
print("a % b = ", remainder)
print("a // b = ", floor_division)
print("a ** b =", exponential)


# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2  # two * sign means exponent or power
print("Are of a circle:", area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("Area of a rectangle:", area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, "N")  # Addign unit to the weight

# Calculating the density of a liquid
mass = 75  # in Kg
volume = 0.075  # in cubic meter
density = mass / volume  # 1000 kg/m^3
print(density, "kg/m^3")


# COMPARISON OPERATORS
print(3 > 2)    # TRue, beacause 3 is greater than 2
print(3 >= 2)   # True, because 3 is greater than 2
print(3 < 2)    #False, because 3 is greater than 2
print(2 < 3)    # True, because 2 is less than 3
print(2 <= 3)   # True, because 2 is less than 3
print(3 == 2)   # False, because 3 is not equal to 2
print(3 != 2)   # True, because 3 is not equal to 2
print(len("mango") == len("avocado"))   # False
print(len("mango") != len("avocado"))   # True
print(len("mango") < len("avocado"))    # True
print(len("milk") != len("meat"))   # False
print(len("milk") == len("meat"))   # True
print(len("tomato") == len("potato"))   # True
print(len("python") > len("dragon"))    # False

# Comparing something gives either a True or False
print("True == True:", True == True)
print("True == False:", True == False)
print("False == False:", False == False)

# LOGICAL OPERATORS
print(3 > 2 and 4 > 3)  # True
print(3 > 2 and 4 < 3)  # False
print("True and True: ", True and True)
print(3 > 2 or 4 > 3)   # True
print(3 > 2 or 4 < 3)   # True
print(3 < 2 or 4 < 3)   # False
print("True or False:", True or False)
print(not 3 > 2)    # False
print(not True)     #False
print(not False)    # True
print(not not True) # True
print(not not False)    # False

