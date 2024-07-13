# Day 11 of 30 Days of Python

# Part 1: add_two_numbers()
import cmath
import math
import statistics
from typing import Counter


def add_two_numbers(num1: float, num2: float):
    return num1 + num2

# Part 2: area_of_circle()
def area_of_circle(radius: float):
    return 3.14 * radius ** 2

# Part 3: add_all_nums() with arbitrary parameters
def add_all_nums(*nums: float):
    sum = 0
    for num in nums:
        sum += num
    return sum

# Part 4: convert_celsius_to_fahrenheit()
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

# Part 5: check_season()
def check_season(month: str):
    month = month.lower()
    if month == 'september' or month == 'october' or month == 'november':
        return 'Autumn'
    elif month == 'december' or month == 'january' or month == 'february':
        return 'Winter'
    elif month == 'march' or month == 'april' or month == 'may':
        return 'Spring'
    elif month == 'june' or month == 'july' or month == 'august':
        return 'Summer'

# Part 6: calculate_slope()
def calculate_slope(x1: float, y1: float, x2: float, y2: float):
    if x1 == x2:
        return 'Undefined'
    return (y2 - y1) / (x2 - x1)

# Part 7: solve_quadratic_equation():
def solve_quadratic_equation(a: float, b: float, c: float):
    if a == 0:
        raise "Coefficient 'a' cannot be zero for a quadratic equation."

    discriminant = b**2 - 4*a*c

    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    return root1, root2

# Part 8: print_list()
def print_list(list: list):
    for item in list:
        print(item)

# Part 9: reverse_list()
def reverse_list(list: list):
    reversed_list = []
    
    for item in list:
        reversed_list.insert(0, item)
    
    return reversed_list

# Part 10: capitalize_list_items()
def capitalize_list_items(list: list):
    for item in list:
        list[list.index(item)] = item.capitalize()

    return list

# Part 11: add_item() to a list
def add_item(list: list, item):
    list.append(item)
    return list

print(add_item(['Hello'], 'World'))

# Part 12: remove_item() from a list
def remove_item(list: list, item):
    if item in list:
        list.remove(item)
    
    return list

# Part 13: sum_of_numbers()
def sum_of_numbers(num: int):
    sum = 0
    
    for i in range(num):
        sum += i
    
    return sum

# Part 14: sum_of_odds()
def sum_of_odds(num: int):
    sum = 0
    
    for i in range(num):
        if i % 2 == 1:
            sum += i

    return sum

# Part 15: sum_of_even()
def sum_of_even(num: int):
    sum = 0
    
    for i in range(num):
        if i % 2 == 0:
            sum += i

    return sum

# ---------------------
# | Exercises Level 2 |
# ---------------------

# Part 1: evens_and_odds()
def evens_and_odds(num: int):
    even_count = 0
    odd_count = 0

    for i in range(num + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Part 2: factorial()
def factorial(num: int):
    if num == 0:
        return 1
    return num * factorial(num -1)

print(f'Factorial of 4: {factorial(4)}')

# Part 3: is_empty() for a list
def is_empty(list: list):
    return not list

print(f'Is the list [] empty: {is_empty([])}')
print(f'Is the list [""] empty: {is_empty([""])}')


# Part 4: Different list functions
def calculate_mean(lst: list):
    if not lst:
        return 'List is empty'
    return sum(lst) / len(lst)

def calculate_median(lst: list):
    if not lst:
        return 'list is empty'
    
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    middle = n // 2
    
    if n % 2 == 0:
        return (sorted_lst[middle - 1] + sorted_lst[middle]) / 2
    else:
        return sorted_lst[middle]

def calculate_mode(list: list):
    # Picked this code from the statistics class
    pairs = Counter(iter(list)).most_common(1)
    
    return pairs[0][0]

def calculate_range(lst: list):
    if not lst:
        return 'List is Empty'
    return max(lst) - min(lst)

def calculate_variance(lst: list):
    if not lst:
        return "List is Empty"
    
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst: list):
    return math.sqrt(calculate_variance(lst))

# ---------------------
# | Exercises Level 3 |
# ---------------------

# Part 1: is_prime()
def is_prime(n: int):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

# Part 2: check_unique()
def is_unique(list: list):
    seen = []
    
    for item in list:
        if item not in seen:
            seen.append(item)
        else:
            return False
    
    return True

# Part 3: is_same_datatype()
def is_same_datatype(list: list):
    seen = set()
    
    for item in list:
        seen.add(type(item))
    
    return len(list) == len(seen)
    

# Part 4: is_valid_variable() 
def is_valid_variable(var):
    valid_types = (int, float, str, bool, list, tuple, dict, set, type(None))
    
    return type(var) in valid_types

# Skipping part 5 as they are the same as before.