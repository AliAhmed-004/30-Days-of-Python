import math

# Exercise Level 1, Part 2
operand1 = 3
operand2 = 4

print(operand1 + operand2)
print(operand1 - operand2)
print(operand1 * operand2)
print(operand1 % operand2)
print(operand1 / operand2)
print(operand1 ** operand2)
print(operand1 // operand2)

# Exercise Level 1, Part 3
name = 'Izuku'
familyName = 'Midoriya'
country = 'Japan'
msg = 'I am enjoying 30 Days of Python'

# Exercise Level 1, Part 4
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(familyName))
print(type(country))

# Exercise level 3, Part 1
print(type(10))                                                     # Integer Example
print(type(1.1))                                                    # Float Example
print(type(4-4j))                                                   # Complex Example
print(type('Hello World'))                                          # String Example
print(type(True))                                                   # Boolean Example
print(type(['Asabeneh', 'Python', 'Finland']))                      # List Example
print(type({'Asabeneh', 'Python', 'Finland'}))                      # Set Example
print(type(('Asabeneh', 'Python', 'Finland')))                      # Tuple Example
print(type({'name': 'Midoriya Izuku', 'course': 'Hero Course'}))    # Dictionary Example


# Exercise level 3, Part 2
point1 = [2, 3]
point2 = [4, 5]

distance = math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))

print(distance)