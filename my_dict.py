dog = {
    "color": "white",
    "breed": "male",
    "legs": 4,
    "age": 110 
}

print(dog)

student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 230,
    "is_married": True,
    "skills": ["Swimming", "Python", "Javascript", "Django"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(len(student))

# Get value of skills and check data types
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 230,
    "is_married": True,
    "skills": ["Swimming", "Python", "Javascript", "Django"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(student.get("skills"))

# Add two skills
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 230,
    "is_married": True,
    "skills": ["Swimming", "Python", "Javascript", "Django"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

student["skills"].append("Angular")
student["skills"].append("Vue")
print(student)

# get dict keys as list
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 230,
    "is_married": True,
    "skills": ["Swimming", "Python", "Javascript", "Django"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(student.keys())

# get dict values as a list
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 230,
    "is_married": True,
    "skills": ["Swimming", "Python", "Javascript", "Django"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(student.values())

# get dict as a list
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 230,
    "is_married": True,
    "skills": ["Swimming", "Python", "Javascript", "Django"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

print(student.items())

# delete one item
# get dict values as a list
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "age": 230,
    "is_married": True,
    "skills": ["Swimming", "Python", "Javascript", "Django"],
    "country": "Kenya",
    "city": "Nairobi",
    "address": {
        "street": "Space Street",
        "zipcode": "10101"
    }
}

# pop()
student.pop("last_name")
student.popitem()
print(student)

# del one dict
dog = {
    "color": "white",
    "breed": "male",
    "legs": 4,
    "age": 110 
}

del dog


