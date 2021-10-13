# © https://sudipghimire.com.np
# %%
"""
# Class

- building block of OOP
- we must instantiate an object for a class to perform specific task



## basic Structure

class <ClassName>:
    <attributes>
    <functions>


# Basic Convention

- Class names are in `UpperCamelCase`
    - MyClass
    - ClassOne
    - Animal
- Attributes (variables & methods) are in `snake_case`
- It is better to have 2 vertical spaces before and after classes
- It is better to have a vertical space before and after methods

"""

# %% example of a class (Animal)
# declaration of class

species_dog = 'dog'
species_man = 'human'


class Animal:
    species = ''  # class attribute (public)
    __legs = 4  # private (accessible only within a class)
    _word = "nothing"  # protected

    # __init__() function
    def __init__(self, name):
        self.name = name  # instance attribute
        pass

    def speak(self):
        print(f'I speak {self._word}')

    def count_legs(self):
        print(f'I have {self.__legs} legs')


# %%
# accessing class attributs
print(Animal.species)  # public
print(Animal._word)  # protected
# print(Animal.__legs)      # unreachable / private

# print(Animal.name)


# %% Instantiating a class
dog = Animal(name="dog")  # dog is an object and Animal is a class
dog.species = 'dog'  # so `dog` is an instance of `Animal`
man = Animal(name='John')
man.species = 'human'

# %% accessing instance attribute
print(dog.name)


# what happens after creating an instance of a class?

# %% __init__() function
# Initializer or constructor


class Animal:
    species = ''  # class attribute (public)
    __legs = 4  # private (accessible only within a class)
    _word = "nothing"  # protected

    # Getter Method
    def get_legs(self):
        return self.__legs

    # Setter Method
    def set_legs(self, legs):
        self.__legs = legs

    # __init__() function
    def __init__(self, name, species, word, legs):
        self.name = name  # instance attribute
        self.species = species
        self._word = word
        self.__legs = legs

    def speak(self):
        print(f'I speak {self._word}')

    def count_legs(self):
        print(f'I have {self.__legs} legs')


john = Animal('John Doe', 'human', 'Hello !!', 2)

# %%

print('Animal: ', Animal.species)
print('John:', john.species)

# changing the instance attribute value
john.name = 'John Lennon'
print('John Name:', john.name)

# getting the private instance attribute

print(john.get_legs())

# %% setting the private instance attribute value
# Wrong method
john.__legs = 3
# lets check how many legs john has

print(john.get_legs())  # returns 2
# it does not change the exact variable we wanted to.
# instead creates different protected variable that is accessible from outside.


# %% right way is to use setter
john.set_legs(3)
# lets check how many legs john has
print(john.get_legs())  # returns 3


# %% more on getter setter

class Students:
    def __init__(self):
        self.students_list = []
        self.teachers_list = ['John', 'Jane']

    def notify_teachers(self, student, status):
        for teacher in self.teachers_list:
            print(f'notify <teacher: {teacher}> that <student: {student}> has {status}')


# %% not a good way
class_1 = Students()

# adding_new_student
new_student = 'Roshan'
class_1.students_list = ['Roshan']
class_1.notify_teachers(new_student, 'joined')

# adding another student
new_student = 'Ashish'
class_1.students_list.append('Ashish')
class_1.notify_teachers(new_student, 'joined')

# removing Ashish from the class
class_1.students_list.remove('Ashish')
class_1.notify_teachers('Ashish', 'left')


# %% we use getter and setter instead
class Students:
    def __init__(self):
        self.__students_list = []
        self.__teachers_list = ['John', 'Jane']

    # changes the string representation of a class
    def __str__(self):
        return f'<Class: Students>'

    def __add__(self, other: 'Students'):
        return [*self.list_students(), *other.list_students()]

    def display_students(self):
        x = [f'{index + 1}\t{student}' for (index, student) in enumerate(self.__students_list)]
        print('\n'.join([f'{index + 1}\t{student}' for (index, student) in enumerate(self.__students_list)]))

    def list_students(self):
        return self.__students_list

    def add_student(self, name):
        self.__students_list.append(name)
        class_1.notify_teachers(name, 'joined')

    def remove_student(self, name):
        self.__students_list.remove(name)
        class_1.notify_teachers(name, 'left')

    def notify_teachers(self, student, status):
        for teacher in self.__teachers_list:
            print(f'notify <teacher: {teacher}> that <student: {student}> has {status}')


# %%
class_2 = Students()
class_3 = Students()

# adding new student
class_2.add_student('Roshan')
class_2.add_student('Ashish')
class_2.add_student('Rocky')
class_2.add_student('Penny')

class_3.add_student('Ram')
class_3.add_student('Shyam')


# %%
class_2.display_students()
# %%
class_2.remove_student('Penny')