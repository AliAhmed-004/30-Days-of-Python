import random
import math

# Part 1 - 3
my_age = 20
my_height = 177.8       # in cm
complex_num = 4j

# Part 4
triangle_base = float(input('Enter base of triangle: '))
triangle_height = float(input('Enter height of triangle: '))
area = 0.5 * triangle_base * triangle_height

print('The area of the triangle is', area)

# Part 5
side_a = float(input('Enter side A of triangle: '))
side_b = float(input('Enter side B of triangle: '))
side_c = float(input('Enter side C of triangle: '))

perimeter = side_a + side_b + side_c
print('The perimeter of triangle is', perimeter)

# Part 6
length = float(input('Enter length of rectangle: '))
width = float(input('Enter width of rectangle: '))

rectangle_area = length * width
rectangle_perimeter = 2*(length + width)
print('Area of Rectangle:', rectangle_area)
print('Perimeter of Rectangle:', rectangle_perimeter)

# Part 7
pi = 3.14
radius = float(input('Enter radius of the circle: '))
area = pi * radius ** 2
circumference = 2 * pi * radius
print('Area of Circle:', area)
print('Circumference:', circumference)

# Part 8
# Define the slope (m) and y-intercept (b) based on the equation y = mx + b
m1 = 2
b = -2

# Calculate the y-intercept (point where x = 0)
y_intercept = (0, b)

# Calculate the x-intercept (point where y = 0)
# Using the equation y = mx + b, set y to 0 and solve for x
# 0 = m * x + b => x = -b / m
x_intercept = (-b / m1, 0)

# Print the results
print(f"Slope (m): {m1}")
print(f"Y-intercept: {y_intercept}")
print(f"X-intercept: {x_intercept}")

# Part 9
point1 = [2, 2]
point2 = [6, 10]

distance = math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))
m2 = (point2[1] - point1[1]) / (point2[0] - point1[0])

# Part 10
print("\nComparison:")
print(f"Slope from Task 8: {m1}")
print(f"Slope from Task 9: {m2}")
print(f"Are the slopes equal? {'Yes' if m1 == m2 else 'No'}")

# Part 11
x = random.randint(0, 10)
y = x**2 + (6*x) + 9

print(y)

# Part 12
str1 = 'Python'
str2 = 'Dragon'

falsy_comparison = len(str1) == len(str2) + 1
print(falsy_comparison)

# Part 13
substring = 'on'

if substring in str1 and substring in str2:
    print(f'{substring} is in both {str1} and {str2}')
else:
    print(f'{substring} is not in {str1} and {str2}')

# Part 14
msg = 'I hope this course is not full of jargon'

if 'jargon' in msg:
    print('True')
else:
    print('False')

# Part 16
text = 'python'
length_in_string = str(float(len(text)))

# Part 17
my_num = 20
if my_num%2 == 0:
    print(f'{my_num} is Even')
else:
    print(f'{my_num} is Odd')

# Part 18
division = 7 // 3
is_equal = division and int(2.7)

# Part 19
print(type('10') and type(10))

# Part 20
print(int('9.8') and 10)

# Part 21
hours = int(input('Enter Hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
pay = hours * rate_per_hour
print(f'Your weekly earning is {pay}')

# Part 22
year = int(input('Enter you age: '))
seconds = year * 365 * 24 * 60 * 60
print(f'You are {seconds} seconds old')

# Part 23
for a in range(1, 6):
    b = 1
    a_squared = a ** 2
    a_cubed = a ** 3
    print(f"{a} {b} {a} {a_squared} {a_cubed}")