# Day 4: 30 Days of Python

# Part 1
str1 = 'Thirty '
str2 = 'Days '
str3 = 'of '
str4 = 'Python'

concatenated_string = str1 + str2 + str3 + str4
print(concatenated_string)

# Part 2
str5 = 'Coding '
str6 = 'For '
str7 = 'All'
concat_string = str5 + str6 + str7

# Part 3 -13
company = 'Coding For All'
print(company)

print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])

if company.find('Coding') != -1:
    print('\'Coding\' is in company')
else:
    print('\'Coding\' is not in company')

company = company.replace('Coding', 'Python')
print(company)

company = company.replace('All', 'Everyone')
print(company)

print(company.split(' '))

# Part 14
companies = 'Facebook, Google, Microsoft, IBM, Oracle, Amazon'
print(companies.split(','))

# Part 15 - 17
print(f'Character at 0th index: \'{company[0]}\'')
print(f'Last index: {len(company) -1}')
print(f'Character at 10th index: \'{company[10]}\'')

# Part 18
acronym = ''.join(word[0] for word in company.split())
print(f'Acronym for \'{company}\' is {acronym}')

# Part 19
name = 'Coding For All'
acronym = ''.join(word[0] for word in name.split())
print(f'Acronym for \'{name}\' is {acronym}')

# Part 20
string = 'Coding For All'
print(f'First occurance of \'C\' in {string}: {string.index('C')}')

# Part 21
string = 'Coding For All'
print(f'First occurance of \'F\' in {string}: {string.index('F')}')

# Part 22
string = 'Coding For All People'
print(f'Last occurance of \'l\' in {string}: {string.rfind('l')}')

# Part 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(f'First occurance of \'because\' in \'{sentence}\': {sentence.index('because')}')

# Part 24
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(f'Last occurance of \'because\' in \'{sentence}\': {sentence.rindex('because')}')

# Part 25
sentence = 'You cannot end a sentence with because because because is a conjunction'
phrase = sentence[sentence.index('because'): sentence.rindex('because')+len('because')]
print(phrase)

# Part 26, 27 Repeated

# Part 28 - 29
string = "Coding For All"
print(string.startswith('Coding'))
print(string.endswith('coding'))

# Part 30
string = '  Coding For All  '
print(f'Before removing spaces: \'{string}\'')
string = string.strip()
print(f'After removing spaces: \'{string}\'')

# Part 31
str1 = '30DaysOfPython'
str2 = 'thirty_days_of_python'

print(f'Is {str1} an identifier: {str1.isidentifier()}')
print(f'Is {str2} an identifier: {str2.isidentifier()}')

# Part 32
python_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join = '# '.join(python_libs)
print(join)

# Part 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# Part 34
print('Name\tAge\tCountry\tCity')
print('John\t35\tFinland\tHelsinki')

# Part 35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

# Part 36
operand1 = 8
operand2 = 6

print('{} + {} = {}'.format(operand1, operand2, operand1 + operand2))
print('{} - {} = {}'.format(operand1, operand2, operand1 - operand2))
print('{} * {} = {}'.format(operand1, operand2, operand1 * operand2))
print('{} / {} = {:.2f}'.format(operand1, operand2, operand1 / operand2))
print('{} % {} = {}'.format(operand1, operand2, operand1 % operand2))
print('{} // {} = {}'.format(operand1, operand2, operand1 // operand2))
print('{} ** {} = {}'.format(operand1, operand2, operand1 ** operand2))