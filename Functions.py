# DECLARING AND CALLING A FUNCTION
# Function without parameters
def generate_full_name():
    first_name = "Jeff"
    last_name = "Gakuya"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function Returning a value
def generate_full_name():
    first_name = "John"
    last_name = "Kush"
    space = " "
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers():
    num_one = 3
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Functions with parameters
def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Jeff'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    print(total)
sum_of_numbers(10)
sum_of_numbers(100)

# Two Parameters
def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print("Full name: ", generate_full_name('Jefferson', 'Gakuya'))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print("Age: ", calculate_age(2021, 1899))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N' # the value has to be changed to a string first
    return weight
print("Weight of an object in Netwons: ", weight_of_object(100, 9.81))

# Passing Arguments with Key and Value
def print_fullname(firtsname, lastname):
    space = ' '
    full_name = firtsname + space + lastname
    print(full_name)
print_fullname(firtsname='Jeff', lastname='Gakuya')

def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)
add_two_numbers(num2=3, num1=5)

# Function Returning Part 2
def print_name(firstname):
    return firstname
print("Jefferson")

# Returning a boolean
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True # return stops further execution of the function, similar to break
    return False
print(is_even(2))  
print(is_even(10))
print(is_even(7))

# Returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Function with default Parameters
def greetings(name = "James"):
    message = name + ", welcome to Python for Everyone!"
    return message
print(greetings())
print(greetings('Jeff'))

def generate_full_name(first_name='James', last_name='Doe'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('DAvid', 'Smith'))

def calculate_age(birth_year, current_year=2021):
    age = current_year - birth_year
    return age;
print("Age: ", calculate_age(1862))

def weight_of_object(mass, gravity=9.81):
    weight = str(mass * gravity) + ' N'
    return weight
print("Weight of an object in Newtons: ", weight_of_object(100))    # 9.81 - average gravity on Earth's surface
print("Weight of an object in Newtons: ", weight_of_object(100, 1.62))  # gravity on the surface of the Moon

# Arbitrary NUmber of Arguments
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num    # same as total = total + num
    return total
print(sum_all_nums(2, 3, 5))

# Default and arbitrary number of parameters in funcions
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team 1', 'Jeff', 'James', 'John', 'DOe')

# Functions as a parameter of another function
def square_number(n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 5))


