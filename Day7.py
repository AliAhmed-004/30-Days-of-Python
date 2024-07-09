# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises Level 1
# Part 1: Length of a set
print(f'Length of \'it_companies\': {len(it_companies)}')

# Part 2: Adding a Company
it_companies.add('Twitter')
print(it_companies)

# Part 3: Adding multiple items
it_companies.update(['Lenovo', 'Dell'])
print(it_companies)

# Part 4: Removing an element
it_companies.remove('Twitter')
print(it_companies)

# Part 5: Difference between Remove and Discard
# Discard will not raise an error if the element is not present, but remove will

# Exercises Level 2
# Part 1: Joining A and B
print(A.union(B))

# Part 2: Intersection
print(A.intersection(B))

# Part 3: Checking subset
print('A is subset  of B' if A.issubset(B) else 'A is not a subset of B')

# Part 4: Checking disjoint
print('A and B are disjoint' if A.isdisjoint(B) else 'A and B are not disjoint')

# Part 5: Joining A with B and B with A
print(f'A Join B {A.union(B)}')
print(f'B Join A {B.union(A)}')

# Part 6: Symmetric Difference Between A and B
print(A.symmetric_difference(B))

# Part 7: Deleting The Sets
del A
del B
del it_companies

#  -------------------
# | Exercises Level 3 |
#  -------------------

# Part 1: Converting ages to a list
age_list = list(age)

print('List of Ages is Longer' if len(age_list) > len(age) else 'Set of Ages is Longer')

# Part 2: Difference between string, list, tuple and set
# String: Immutable, ordered sequence of characters. Allows duplicates. Supports indexing and slicing.
# List: Mutable, ordered sequence of items. Allows duplicates. Supports indexing and slicing.
# Tuple: Immutable, ordered sequence of items. Allows duplicates. Supports indexing and slicing.
# Set: Mutable, unordered collection of unique items. Does not allow duplicates. Does not support indexing or slicing.

# Part 3: Analyze the given string
string = 'I am a teacher and I love to inspire and teach people'
splitted_string = string.split(' ')
unique_words = set(splitted_string)

print(f'Unique words in given String: {unique_words}')
