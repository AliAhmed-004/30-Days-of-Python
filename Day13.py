# Day 13 of 30 Days of Python: List Comprehension and Lambda Functions
# ---------------------
# | Exercises Lavel 1 |
# ---------------------

# Part 1: Filtering negatives and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [ i for i in numbers if i > 0] 

print(f'\nUnfiltered numbers: {numbers}')
print(f'Filtered numbers: {filtered_numbers}')

# Part 2: Flattening a List
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_list = [item for sublist1 in list_of_lists for sublist2 in sublist1 for item in sublist2]

print(flat_list)

# Part 3: Creating a list of lists of tuple
list = [(i, 1, i**2, i**3, i**4, i**5) for i in range(11)]

print('\nList of lists of tuple:')
for row in list:
    print(row)

# Part 4: Flattening a List Pt. 2
print('\nFlattening a List of Lists of Tuple')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_list = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

print(flat_list)

# Part 5: Transforming a list to a dictionary
print('\nTransforming a List to a Dictionary:')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flat_list = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

print(flat_list)

# Part 6: Creating concatenated strings for a List of Lists of Tuple
print('Concatenated Names:')
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

concatenated_names = [first_name + ' ' + last_name for sublist in names for first_name, last_name in sublist]

print(concatenated_names)

# Part 7: Lambda function for slope
print('\nSlope of (10, 20) and (30 40) is ', end = '')
slope = lambda x1, y1, x2, y2: (x2-x1) / (y2 - y1)

print(slope(10, 20, 30, 40))

