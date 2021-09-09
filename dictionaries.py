# Creating a Dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(len(person))

# Accessing Dictionary Items
print(person["first_name"])
print(person["country"])
print(person["skills"])
print(person["skills"][0])
print(person["address"]["street"])

# get() Method
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(person.get("first_name"))
print(person.get("country"))
print(person.get("skills"))
print(person.get("city"))

# Adding Items to a dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

person["job_title"] = "Junior Software Engineer"
person["skills"].append("HTML")
print(person)

# modifying Items in a Dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

person["first_name"] = "Kyle"
person["age"] = 240
print(person)

# Checking Keys in a Dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print("first_name" in person)
print("middle_name" in person)

# Removing Key and Value Pairs from a Dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

# pop()
person.pop("first_name")    # removes specified key name
person.popitem()    # removes the last item
del person["is_married"]    # removes a specified key name
print(person)

# Changing Dictionary to a List Items
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(person.items())

# Clearing a Dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(person.clear())

# Deleting a Dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

del person

# Copy a Dictionary
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

person_copy = person.copy()
print(person_copy)

#   Getting Dictionary Keys as a List
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

keys = person.keys()
print(keys)

# Getting Dictionary values as a List
person = {
    "first_name": "Jefferson",
    "last_name": "Gakuya",
    "age": 230,
    "country": "Nairobi",
    "is_married": False,
    "skills": ["Python", "Django", "Javascript", "Angular", "Vue", "Postgres"],
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

values = person.values()
print(values)

