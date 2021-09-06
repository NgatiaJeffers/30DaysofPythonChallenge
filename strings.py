# Creating a String
greeting = "Hello, World!"
print(len(greeting))

sentence = "I hope one day I become a world class developer."
print(sentence)

multiline_string = """I am a student and enjoy learning. 
I try hard and learn Python, its sweet just like other
programming languages. That is why, I'm tring my best and
learn Python language. All the best Jeff."""
print(multiline_string)

# Stirng Concatenation
first_name = "Jefferson"
last_name = "Gakuya"
space = " "
full_name = first_name + space + last_name

print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

# Escape Sequence in Strings
print("I am enjoying this Python Challenge day in day out.\nAre you ?")
print("Days\tTopics\tExercises")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Day 3\t3\t5")
print("Day 4\t3\t5")
print("This is a backslash symbol (\\)")
print("In every programming language it starts with \'Hello, World!\'")

# String Formating
first_john_name = "John"
last_doe_name = "Doe"
language = "Python"
formated_string = "I am %s %s. I teach %s" %(first_john_name, last_doe_name, language)
print(formated_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "This area of circle with a radius %d is %.2f." %(radius, area)

python_libraries = ["Django", "Flask", "Numpy", "Pandas"]
formated_string = "The following are Python Libraries:%s" %(python_libraries)
print(formated_string)

# NEw Style String Formating(str.format)
formated_string = "I am {} {}. I love {}".format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

formated_string = "The area of a circle with a radius {} is {:.2f}".format(radius, area)
print(formated_string)

# Stirng Interpolation
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}') # limits it to two digits after decimal
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} + {b} = {a + b}')
print(f'{a} + {b} = {a + b}')

# Unpacking Characters
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing Characters in Strings by Index
language = "Python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

# Slicing Python Strings
language1 = "Javascript"
first_four = language1[0:4]
last_six = language1[4:10]
print(last_six)

# refactor
last_six = language1[-6:]
print(last_six)
last_six = language1[4:]
print(last_six)

# Reversing a String
greeting = "Hello, World!"
print(greeting[::-1])

# Skipping Characters While Slicing
language = "Python"
pto = language[0:6:2]
print(pto)


# String Methods
challenge = "thirty days of python"
print(challenge.capitalize())
# Count()
print(challenge.count("y"))
print(challenge.count("y", 9, 14))
print(challenge.count("th"))
# endswith()
print(challenge.endswith("on"))
print(challenge.endswith("tion"))
# expandtabs
challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(10))
# find()
print(challenge.find("y"))
print(challenge.find("th"))
# rfind()
print(challenge.rfind("y"))
print(challenge.rfind("th"))
# index()
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index(sub_string))
# isalnum()
challenge1 = "ThirtyDaysPython"
print(challenge1.isalnum())
# isalpha()
print(challenge.isalpha())
print(challenge1.isalpha())

num = "123"
print(num.isalpha())

# join()
web_tech = ["HTML", "CSS", "Javascript", "React"]
result = "#".join(web_tech)
print(result)

# strip()
challenge = "thirty days of python"
print(challenge.strip("noth"))

# replace()
print(challenge.replace("python", "coding"))

# Split()
print(challenge.split())
challenge = "thirty, days, of, python"
print(challenge.split(", "))

# title()
print(challenge.title())

# swapcase()
challenge = "thirty days of python"
print(challenge.swapcase())
challenge = "Thirty Days Of Python"
print(challenge.swapcase())

# startwith()
challenge = "thirty days of python"
print(challenge.startswith("thirty"))
challenge = "30 days of python"
print(challenge.startswith("thirty"))


