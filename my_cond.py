age = float(input("Enter your age: "))
remainder = int(18 % age)
if age >= 18:
    print("Your are old enough to learn to drive.")
else:
    print("You need", remainder, "more years to learn to drive")


# Compare ages
my_age = float(input("My age: "))
your_age = float(input("Your Age: "))
remainder = int(your_age - my_age)
if my_age > your_age:
    if my_age % your_age == remainder:
        print("Your are", remainder, "years older than me")
    else:
        print("I'm older than you")
elif your_age > my_age:
    print("I'm older than you")
else:
    print("We are of the same age")

# Another compare
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))
if a > b:
    print(int(a), "is greater than", int(b))
elif a < b:
    print(int(a), "is smaller than", int(b))
else:
    print(int(a), "is equal to", int(b))

# Grading Students
score = float(input("Enter your score: "))
if score >= 80:
    print("You have A grade")
elif score >= 70:
    print("You have B as your grade")
elif score >= 60:
    print("Your score is C")
elif score >= 50:
    print("Your score is D")
else:
    print("You scored an F")

# Check Seasons Date
season = input("Enter any month to get the season: ")
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
if season in autumn:
    print("The month your typed is in the Autumn category")
elif season in winter:
    print("The month you typed is in the Winter category")
elif season in spring:
    print("The month you typed is in the Spring category")
else:
    print("This month is in the Summer category")

# Check if fruit exits, if it doesn't, we add to the List
fruits = ["banana", "orange", "mango", "lemon"]
fruit = input("Check a fruit in the store: ")
if fruit in fruits:
    print("Your fruit is already in the list", fruits)
elif fruits.append(fruit):
    print("We didn't find the fruit but we added your fruit in the list", fruits)
else:
    print("Here is the fruits list", fruits) 

# A personal dictionary, modifying it
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 240,
    "country": "Kenya",
    "is_married": False,
    "skills": ["Python", "Javascript", "Django", "Vue", "Angular", "Flask"],
    "address": {
        "street": "Space street",
        "zipcode": "02201"
    }

}

skills_keys = person.get("skills")
print("Here is the skills keys", skils_keys)

