name = 'Stranger'
age = 30

# not pythonic!
print('Hi there ' + name + ' I see you are ' + str(age) + ' years old!')

# p2 style
print('Hi there %s I see you are %s years old!' % (name, age))

print('Hi there {} I see you are {} years old!'.format(name, age))

data = {
    'name': 'Stranger',
    'age': 30
}

print('Hi there {name} I see you are {age} years old!'.format(**data))

# Python 3.6 only...
print(f"HI there {name.upper()} I see you are {(str(age) + ' year' if age == 1 else str(age) + ' years')} old.")

