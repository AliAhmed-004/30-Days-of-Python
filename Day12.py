# Day 12 of 30 Days of Python Challenge

import random
import string

# ---------------------
# | Exercises Level 1 |
# ---------------------

# Part 1: Generete id
def random_user_id():
    length = 6
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(length))
    return user_id

print(f'Random User ID: {random_user_id()}')

# Part 2: Custom length and no of IDs
def user_id_gen_by_user():
    length = int(input("Enter length of ID: "))
    no_of_ids = int(input("Enter number of IDs to generate: "))

    user_ids = []
    
    for i in range(no_of_ids):
        characters = string.ascii_letters + string.digits

        user_id = ''.join(random.choice(characters) for _ in range(length))

        user_ids.append(user_id)

    return user_ids

# print(user_id_gen_by_user())

# Part 3: Random Color Generator
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return f'rgb({red}, {green}, {blue})'

def random_rgb_color_gen(num_of_colors=1):
    return [rgb_color_gen() for _ in range(num_of_colors)]

rgb_color_gen()

# ---------------------
# | Exercises Level 2 |
# ---------------------

# Part 1: Generating hexa colors
def random_hex_color():
    hex_digits = '0123456789abcedf'
    
    hex_color = ''.join(random.choice(hex_digits) for _ in range(6))
    
    return f'#{hex_color}'

# Part 2: Any number of hex colors
def list_of_hex_colors(num_of_colors = 1):
    return [random_hex_color() for _ in range(num_of_colors)]

print(list_of_hex_colors(3))
print(list_of_hex_colors())

def generate_colors(type: str, num_of_colors: int):
    if type == 'hexa':
        return list_of_hex_colors(num_of_colors)
    elif type == 'rgb':
        return random_rgb_color_gen(num_of_colors)

print()
print(generate_colors('hexa', 3))
print(generate_colors('rgb', 3))

# ---------------------
# | Exercises Level 3 |
# ---------------------

# Part 1: Method to Shuffle a list
def shuffle_list(list: list):
    
    length_of_list = len(list)
    shuffled_list = []
    
    while(len(shuffled_list) != length_of_list):
        item = random.choice(list)
        list.remove(item)
        
        shuffled_list.append(item)
    
    return shuffled_list

print(f'Original List: {[1,2,3,4,5,5]}')
print(f'Shuffeled List: {shuffle_list([1,2,3,4,5,5])}')

# Part 2: Seven Deadly 'Numbers'
def seven_random_numbers():
    random_numbers = set()
    length = 7
    
    while(len(random_numbers) != length):
        random_numbers.add(random.randint(0, 9))
    
    return random_numbers

print(f'7 Random Numbers: {seven_random_numbers()}')
