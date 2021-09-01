# Variables
first_name = "Jefferson"
last_name = "Gakuya"
country = "Kenya"
city = "Nairobi"
age = 230
is_married = False
skills = ["HTML", "CSS", "JS", "Python", "Django", "Angular"]
personal_info = {
    "firstname": "Jefferson",
    "lastname": "Gakuya",
    "country": "Kenya",
    "city": "Nairobi"
}

print("First name:  ", first_name, type(first_name))
print("First name length:  ", len(first_name))
print("Last name:  ", last_name)
print("Last name length:  ", len(last_name))
print("Country:  ", country)
print("City:  ", city)
print("Age:  ", age)
print("Married:  ", is_married)
print("Skills:  ", skills)
print("Personal Information:  ", personal_info)

# Getting user input
my_first_name = input("What is your name: ")
my_age = input("How old are you? ")

print(my_first_name)
print(my_age)


# Casting
# int to float
num_int = 10
print("num_int", num_int)
num_float = float(num_int)
print("num_float:", num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int = 10
print(num_int)
num_str = str(num_int)
print(num_str, type(num_str))

# str to int or float
num_in_str = "10"
print("num_int", int(num_in_str))
print("num_float", float(num_in_str))

# str to list
my_first_name = "Jefferson the Coder"
print(my_first_name)
first_name_to_list = list(my_first_name)
print(first_name_to_list)

