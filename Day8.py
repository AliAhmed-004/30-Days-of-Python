# Day 8: Dictionaries

# -------------
# | Exercises |
# -------------
# Part 1: Creating an empty Dictionary
dog = {}

# Part 2: Adding key-value pairs
dog = {
    'name': 'Sunshine',
    'color': 'Golden',
    "breed": 'Golden Retriever',
    'legs': 4,
    'age': 5
}

# Part 3: Student Dictionary
student = {
    'first_name': 'Ali',
    'last_name': 'Ahmed',
    'gender': 'male',
    'age': 20,
    'marital_status': 'single',
    'skills': ['Java', 'Flutter', 'Python'],
    'country': 'Pakistan',
    'city': 'Islamabad',
    'address': 'Above Earth, below sky'
}

# Part 4: Length of dictionary
print(f'\nLength of Student Dictionary: {len(student)}')

# Part 5: Checking a value
print(f'\nSkills: {student.get('skills')}')
print(f'\nType of Skills: {type(student.get('skills'))}')

# Part 6: Adding new skills
student['skills'].append('C++')
student['skills'].append('HTML')

print(f'\nNew Skills: {student.get('skills')}')

# Part 7: Getting keys as list
student_keys = list(student.keys())
print(f'\nKeys: {student_keys}')

# Part 8: Getting values as list
student_values = list(student.values())
print(f'\nValues: {student_values}')

# Part 9: List of tuples
student_list_of_tuples = list(student.items())
print(f'\nList of Tuples: {student_list_of_tuples}')

# Part 10: Deleting one item
student.pop('address')
print(f'\nUpdated Student: {student}')

# Part 11: Deleting a Dictionary
del student
