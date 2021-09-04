my_age = 23
my_height = float(56)
my_complex = 1 + 1j

base = float(input("Enter the base: "))
height = float(input("Enter the height: "))

# calculate the area
area = int((base * height) * 0.5)

print("The area of the triangle is ", area)

# Perimeter
side_a = float(input("Enter side A: "))
side_b = float(input("Enter side B: "))
side_c = float(input("Enter side C: "))

perimeter = int(side_a + side_b + side_c)

print("The perimeter of the triangle is ", perimeter)

# Calculate area of a triangle
triangle_length = float(input("Click on that length number: "))
triangle_height = float(input("Click on that height number: "))

area_of_triangle = int(triangle_length * triangle_height)

print("The area of the triangle is ", area_of_triangle)

# Finding the triangles perimeter

perimeter_of_triangle = int(triangle_length + triangle_height) * 2

print("Triangles of perimeter ", perimeter_of_triangle)


# Area of circle
pi = 3.14
radius = float(input("Enter your radius: "))
area_of_circle = int(pi * radius * radius)

circumference = int(pi * radius) * 2

print("Area of a circle: ", area_of_circle)
print("Circumference: ", circumference)


