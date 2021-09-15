# Break
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Continue
# count = 0
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1

# For Loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# For loop with string
language = "Python"
for letter in language:
    print(letter)

# For loop with tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dict
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 240,
    "country": "Kenya",
    "is_married": False,
    "skills": ["Python", "Javascript", "Vue", "Angular", "Flask"],
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    }
}

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)   # this way we get both keys and values printed out

# Loops in set
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
for company in it_companies:
    print(company)

# Break and Continue
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number ==3:
        break
# continue
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number ==3:
        continue
    print("Next number should be ", number + 1) if number != 5 else print("loop's end") # for short hand conditions need both id and else statement
print("Outside the loop")


# THE RANGE FUNC
# Creating sequences using range
lst = list(range(11))
print(lst)

st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst)

st = set(range(0,11,2))
print(st)

# for and range
for number in range(11):
    print(number)

# Nested For Loop
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 240,
    "country": "Kenya",
    "is_married": False,
    "skills": ["Python", "Javascript", "Vue", "Angular", "Flask"],
    "address": {
        "street": "Space street",
        "zipcode": "02210"
    }
}
for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

# For Else
for number in range(11):
    print(number)
else:
    print("The loop stops at", number)

# Pass
for number in range(6):
    pass

