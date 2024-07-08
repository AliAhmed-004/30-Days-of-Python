# --------------------
# | Exercise Level 1 |
# --------------------
# Part 1: Creating an empty tuple
my_tuple = ()

# Part 2: Creating initialized tuple
brothers = ('Monjiro', 'Tanjiro', 'Zenitsu')
sisters = ('Nezuko', 'Kanao')

# Part 3: Joining the tuples
siblings = brothers + sisters

# Part 4: Counting the siblings
print(f'I have {len(siblings)} siblings')

# Part 5: Modifying the tuple
# Since tuples are immutable (cannot be modified), We cannot add or remove elements from a tuple.

# --------------------
# | Exercise Level 2 |
# --------------------

family_members = siblings + ('Muzan Kibutsuji', 'Tamao')

# Part 1: Unpacking a tuple
bro1, bro2, bro3, sis1, sis2, dad, mom = family_members
print(f'Bro1: {bro1}')
print(f'Bro2: {bro2}')
print(f'Bro3: {bro3}')
print(f'Sis1: {sis1}')
print(f'Sis2: {sis1}')
print(f'Mom: {mom}')
print(f'Dad: {dad}')

# Part 2: Fruits, veggies, animal_products
fruits = ("apple", "banana", "cherry", "date", "grape")
vegetables = ("carrot", "broccoli", "spinach", "pepper", "onion")
animal_products = ("milk", "cheese", "yogurt", "eggs", "chicken")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Part 3: Tuple -> List
food_stuff_lst = list(food_stuff_tp)

# Part 4: Middle food(s)
middle_food_index = len(food_stuff_lst) // 2

if middle_food_index % 2 == 0:
    print(f'Middle  Foods: {food_stuff_lst[middle_food_index : middle_food_index + 1]}')
else:
    print(f'Middle Food: {food_stuff_lst[middle_food_index]}')

# Part 5: Slicing a tuple
first_three_elements = food_stuff_lst[ : 3]
last_three_elements = food_stuff_lst[-3:]

print(f'First 3 Elements: {first_three_elements}')
print(f'Last 3 Elements: {last_three_elements}')

# Part 6: Deleting the Tuple
del food_stuff_tp

# Part 7: Checking if an element is in a tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print('Estonia is a Nordic Country')
else:
    print('Estonia is not a Nordic Country')

if 'Iceland' in nordic_countries:
    print('Iceland is a Nordic Country')
else:
    print('Iceland is not a Nordic Country')