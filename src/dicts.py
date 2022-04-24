# Dictionaries
my_dict = {
    'hello' : 'hello',
    'hi' : 'hi',
    'hey': 'hey'
}

print(my_dict)

# --------------
for k, v in my_dict.items():
    print('%s %a' % (k, v))

# --------------
del my_dict['hi'] # or my_dict.pop('hi')
print(my_dict)
