# Day 9 of 30 Days of Python Challenge
# ---------------------
# | Exercises Level 1 |
# ---------------------

# Part 1: Can you drive yet?
age = int(input("Enter your age: "))

if age >= 18:
    print('You are old enough to learn to drive\n')
else:
    print(f'You need {18 - age} more years to learn to drive\n')

# Part 2: Who's Older?
my_age = 20
your_age = int(input("Enter your age: "))

if my_age == your_age:
    print("We have the same age!")
elif my_age > your_age:
    print(f'I am {my_age - your_age} years older than you!\n')
else:
    print(f'You are {your_age - my_age} years older than me!\n')

# Part 3: Which number is greater?
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a > b:
    print(f'{a} is greater')
elif a < b:
    print(f'{b} is greater')
else:
    print(f'{a} and {b} are equal')

# ---------------------
# | Exercises Level 2 |
# ---------------------

# Part 1: Grading Students
marks = int(input("Enter your total marks: "))

if marks >= 80 and marks <= 100:
    print("Grade: A")
elif marks >= 70 and marks <= 79:
    print("Grade: B")
if marks >= 60 and marks <= 69:
    print("Grade: C")
if marks >= 50 and marks <= 59:
    print("Grade: D")
else:
    print("Grade: F")

# Part 2: Check the Season
month = input('Enter the month: ')
month = month.lower()

if month == 'september' or month == 'october' or month == 'november':
    print('Season: Autumn')
elif month == 'december' or month == 'january' or month == 'february':
    print('Season: Winter')
elif month == 'march' or month == 'april' or month == 'may':
    print('Season: Spring')
elif month == 'june' or month == 'july' or month == 'august':
    print('Season: Summer')

# Part 3: FRUITS!!
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ")

if fruit in fruits:
    print('This fruit exists')
else:
    fruits.insert(len(fruits), fruit)
    print(f'Updated Fruits: {fruits}')

# ---------------------
# | Exercises Level 3 |
# ---------------------

# Part 1: Analyzing a Person
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person.keys():
    skills = person['skills']
    middle_skill = len(skills) // 2
    if len(skills) % 2 == 0:  # even number of skills
        print(f'Middle Skills: {skills[middle_skill - 1]} and {skills[middle_skill]}')
    else:  # odd number of skills
        print(f'Middle Skill: {skills[middle_skill]}')
else:
    print('No skills found')

# Part 2: Checking for a specific skill
if 'skills' in person.keys():
    skills = person['skills']

    if 'Python' in skills:
        print(f'{person["first_name"]} knows Python')
    else:
        print(f'{person["first_name"]} does not know Python')
else:
    print('No skills found')

# Part 3: What does the person do?
if 'skills' in person:
    skills = set(person['skills'])
    
    front_end_skills = {'JavaScript', 'React'}
    back_end_skills = {'Node', 'Python', 'MongoDB'}
    fullstack_skills = {'React', 'Node', 'MongoDB'}
    
    # Check for front end developer skills
    if front_end_skills.issubset(skills) and not back_end_skills.intersection(skills):
        print('He is a front end developer')
    # Check for back end developer skills
    elif back_end_skills.issubset(skills) and not front_end_skills.intersection(skills):
        print('He is a backend developer')
    # Check for full stack developer skills
    elif fullstack_skills.issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print('No skills found')

# Part 4: Married? Where living?
if person['is_marred']:
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married.')
else:
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is not married.')
