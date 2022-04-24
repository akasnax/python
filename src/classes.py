# Classes

class PythonGuide:
    something = 'something'

    def func(self):
        print('Hi, I am a Python guide!')


my_python_guide = PythonGuide()
my_fake_python_guide = PythonGuide()

my_fake_python_guide.something = 'not something'

print(my_python_guide.something)
print(my_fake_python_guide.something)

my_python_guide.func()