# Day 2: 30 Days of Python Challenge
# Exercise Level 1
firstName = 'Gojo'
lastName = 'Saturo'
fullName = firstName + ' ' + lastName
country = 'Japan'
city = 'Shibuya'
age = 28
birthYear = 1996
is_married = False
is_true = True
is_light_on = False
birthMonth, dateOfBirth = 'December', '7 December, 1996'

# Exercise Level 2
# Part 1
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(birthMonth))
print(type(birthYear))

# Part 2
print(len(firstName))

# Part 3
if len(firstName) > len(lastName):
    print('First Name is longer')
elif len(firstName) < len(lastName):
    print('Last Name is longer')
else:
    print('Both are equal in length')

# Part 4
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

# Part 5
radius  = 30
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius

user_radius = int(input('Enter Radius of Circle: '))
area_of_user_circle = 3.14 * (user_radius ** 2)

# Part 6
user_first_name = input('Enter your First Name: ')
user_last_name = input('Enter your Last Name: ')
user_country = input('Enter your Country: ')
user_age = int(input('Enter your Age: '))

# Part 7
help('keywords')