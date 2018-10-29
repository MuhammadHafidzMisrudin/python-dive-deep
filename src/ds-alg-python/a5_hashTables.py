
# Declaring a dictionary
dictStudent = {'Name':'Zara', 'Age':'20', 'Class':'first'}
print('\n')

# Accessing the dictionary with its value
print('dictStudent[Name] = ', dictStudent['Name'])
print('dictStudent[Age] = ', dictStudent['Age'])
print('dictStudent[Class] = ', dictStudent['Class'])
print('\n')

# Check if the given key exists.
# Way: 1.
if 'Age' in dictStudent:
    print('Key : {0} => does exit'.format('Age'))
else:
    print('Key does NOT exit')

print('\n')

# Way: 2.
for key, name in dictStudent.items():
    if name == 'Zara':
        print('Key: ', key)
        break
    else:
        print('Key not exists')

# Add new entry.
dictStudent['University'] = 'QUT'

print('\n')
for x,y in dictStudent.items():
    print('{0} = {1}'.format(x, y))

print('\n')
