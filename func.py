# EXERCISE
# 1
def add_two_numbers(a, b):
    sum = a + b
    return sum
print(add_two_numbers(2, 5))

# 2
def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

# 3
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
        if isinstance(num, int):
            return "Its an Integer"
        if isinstance(num, str):
            return "Its a stirng"
        if isinstance(num, float):
            return "Its a floating number"
print(add_all_nums(1, 2, 3))

# 4
def convert_celcius_to_fahrenheit(c):
    fah = float(c * 9/5) + 32
    return fah
print(convert_celcius_to_fahrenheit(32), "F")

# 5
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
def check_season(month):
    if month in autumn:
        return month + " is an Autumn month"
    elif month in winter:
        return month + " is a Winter month"
    elif month in spring:
        return month + " is a Spring month"
    else:
        return month + " is a Summer month"
print(check_season("November"))

# 6
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1)/(x2 - x1)
    return slope
print(calculate_slope(2, 3, 6, 7))

# 7
# def solve_quadratic_eqn(a, b, c):
#     eq = 
# print(solve_quadratic_eqn(2, 2, 2))

# 8
def print_list(stack, *args):
    print(stack)
    for i in args:
        print(i)
print_list('Python', 'Javascript', 'Vue', 'Angular')

# 9

