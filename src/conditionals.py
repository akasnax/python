# Conditionals

my_num = 30
my_prr = 'prr'
my_meow = 'meow'
my_hello = 'hello'

if my_num == 30:
    print('hi!')
else:
    pass

if my_meow == 'meow' or my_prr == 'prr':
    print('meowmeow!')

if my_meow == 'maow' or my_hello == 'hello':
    print('almost not, but meowmeow!')

if not my_meow in ['maow', 'mew']:
    print('not meowmeow?')