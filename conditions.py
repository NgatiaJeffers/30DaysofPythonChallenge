# IF Condition
a = 3
if a > 0:
    print("A is a positive number")

# IF ELSE condiotion
a = 3
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")


# IF ELIF ELSE
a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")

# Short Hand
a = 3
print("A is positive") if a > 0 else print("A is negative")

# Nested Condition
a = 0
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even integer")
    else:
        print("A is a positive number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")

# IF condition AND Logical Operators
a = 2
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
elif a == 0:
    print("A is zero")
else:
    print("A is negative")

# IF and OR Logical Operators
user = "James"
access_level = 3
if user == "admin" or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")
