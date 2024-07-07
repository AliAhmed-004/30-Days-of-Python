# Day 5: 30 Days of Python

# EXERCISE LEVEL 1 <---------------------->
# Part 1 - 4
empty_list = []

longer_list = ['Demon Slayer', 'Attack on Titan', 'My Hero Academia', 'Death Note', 'Tokyo Revengers']

print(f'First Element: {longer_list[0]}')
print(f'Last Element: {longer_list[longer_list.__len__()-1]}')
print(f'Middle Element: {longer_list[longer_list.__len__() // 2]}')

# Part 5
mixed_data_type_list = ['Bakugo', 17, 5.5, 'Single', 'Japan']

# Part 6 - 27
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)
print(f'Number of Companies: {len(it_companies) - 1}')

print(f'First Company: {it_companies[0]}')
print(f'Last Company: {it_companies[it_companies.__len__()-1]}')
print(f'Middle Company: {it_companies[it_companies.__len__() // 2]}')

it_companies[3] = 'Redmi'
print(it_companies)

it_companies.append('Apple')
print(it_companies)

it_companies[len(it_companies) // 2] = 'Techno'
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

companies = '# '.join(it_companies)
print(companies)

print('IBM' in it_companies)
print('Redmi' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

slice_of_companies = it_companies[0 : 3]
print(slice_of_companies)

slice_of_companies = it_companies[-3:]
print(slice_of_companies)

slice_of_companies = it_companies[len(it_companies) // 2: len(it_companies) // 2 + 1]
print(slice_of_companies)

it_companies.remove(it_companies[0])
print(it_companies)

length = len(it_companies)
middle_index = length // 2

if middle_index % 2 == 0:
    del it_companies[middle_index - 1 : middle_index + 1]
else:
    del it_companies[middle_index]

print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

try:
    print(it_companies)
except NameError as e:
    print(f'Error: {e}')

# Part 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')

print(full_stack)

# EXERCISES LEVEL 2 <--------------------------
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sorting the list
ages.sort()

# Finding min and max ages
minAge = ages[0]
maxAge = ages[-1]

print(f'Minimum Age: {minAge}')
print(f'Maximum Age: {maxAge}')

# Adding min and max ages to the list
ages.insert(len(ages) - 1, minAge)
ages.insert(len(ages) - 1, maxAge)

# Finding median age
number_of_ages = len(ages)
median_age = number_of_ages // 2

if median_age % 2 == 0:
    print(f'Median ages: {ages[median_age - 1 : median_age + 1]}')
else:
    print(f'Median Age: {ages[median_age]}')

# Finding the average age
average_age = 0
for age in ages:
    average_age += age

average_age = average_age // len(ages)
print(f'Average age: {average_age}')

# Finding Range of Ages
ages.sort()

range_of_ages = [ages[0], ages[-1]]

print(f'Range of Ages: {range_of_ages}')

# Comparing values
absolute_min_difference = abs(minAge - average_age)
absolute_max_difference = abs(maxAge - average_age)

print(f'Absoluter Minimum Difference: {absolute_min_difference}')
print(f'Absoluter Maximum Difference: {absolute_max_difference}')

# Finding the middle Country/Countries
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

number_of_countries = len(countries)
middle_country = number_of_countries // 2

if middle_country % 2 == 0:
    print(f'Middle Countries: {countries[middle_country - 1 : middle_country + 1]}')
else:
    print(f'Middle Country: {countries[middle_country]}')

# Dividing the Countries list in two
if middle_country % 2 == 0:
    first_half = countries[ : middle_country]
    second_half = countries[middle_country : ]
else:
    first_half = countries[ : middle_country + 1]
    second_half = countries[middle_country + 1 : ]

print(f'First Half: {first_half}')
print(f'Second Half: {second_half}')

# Unpacking a List
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = countries

print(f'First Country: {first_country}')
print(f'Second Country: {second_country}')
print(f'Third Country: {third_country}')
print(f'Scandic Countries: {scandic}')