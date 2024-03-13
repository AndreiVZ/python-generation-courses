# ----------------------------------------
print(f'{bin(123 << 1)[2:]:>09}')   # 011110110 246
print(f'{bin(123 >> 1)[2:]:>09}')   # 000111101 61

print(f'{bin(123)[2:]:>09}')        # 001111011 123
print(f'{bin(456)[2:]:>09}')        # 111001000 456

print(f'{bin(123 & 456)[2:]:>09}')  # 001001000 72
print(f'{bin(123 | 456)[2:]:>09}')  # 111111011 507
print(f'{bin(123 ^ 456)[2:]:>09}')  # 110110011 435
# ----------------------------------------
original = [1, 2, 3]
other = original
original[:] = [0, 0]  # the same list
print(id(original) == id(other))  # True

original = [1, 2, 3]
other = original
original = [0, 0]  # new list
print(id(original) == id(other))  # False
# ======================================== 2.1
x = int(input())
for i in range(x):
    for j in range(x):
        print(min(i + 1, j + 1, x - i, x - j), end=' ')
    print()
# ----------------------------------------
x = input()
for _ in range(10):
    x = x.replace('()', '')
print('False' if x else 'True')


x = input()
while '()' in x:
    x = x.replace('()', '')
print('False' if x else 'True')
# ----------------------------------------
def inversions(seq):
    return sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq)) if seq[i] > seq[j])


from itertools import combinations
def inversions(sequence: list[int]) -> int:
    result = 0
    for seq in combinations(sequence, 2):
        current_item, next_item = seq
        if current_item > next_item:
            result += 1
    return result
# ----------------------------------------
list_ = open(0).read().split('\n')
print(len(list_) - len(set(list_)))


import sys
pokemons = [pokemon.strip() for pokemon in sys.stdin]
print(len(pokemons) - len(set(pokemons)))
# ----------------------------------------
import json, functools
def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return json.dumps(value)
    return wrapper
# ----------------------------------------
list_ = open(0).read().split('\n')
for i in list_:
    x, y = map(float, i.strip('()').split(', '))
    print(-90 <= x <= 90 and -180 <= y <= 180)
# ----------------------------------------
def quantify(iterable, predicate):
    return sum((predicate if predicate else bool)(i) for i in iterable)
# ----------------------------------------
from datetime import date, timedelta
year, month = int(input()), int(input())
dates = [date(year, month, day=i) for i in range(1, 29) if date(year, month, day=i).weekday() == 3] 
print(dates[3].strftime('%d.%m.%Y'))
# ----------------------------------------
import re
def is_integer(string):
    return bool(re.search(f'^-?[0-9]+$', string))
#   return True if re.search(f'^-?[0-9]+$', string) else False


import re
def is_integer(string: str) -> bool:
    regex_obj = re.compile(r'-?\d+')
    return bool(regex_obj.fullmatch(string))


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
# ----------------------------------------
import re
def is_decimal(string):
    return bool(re.fullmatch(f'-?[0-9]+\.?[0-9]*|-?[0-9]*\.?[0-9]+', string))


import re 
def is_decimal(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
# ----------------------------------------
import re
def is_fraction(string):
    return bool(re.fullmatch(f'-?[0-9]+/0*[1-9]+[0-9]*', string))


from fractions import Fraction
def is_fraction(string):
    try:
        Fraction(string)
        return '/' in string
    except (ValueError, ZeroDivisionError):
        return False
# ----------------------------------------
def intersperse(iterable, delimiter):
    iterator = iter(iterable)
    try:
        yield next(iterator)
        while True:
            next_iterator = next(iterator)
            yield delimiter
            yield next_iterator
    except StopIteration:
        return


def intersperse(iterable, delimiter):
    for i, v in enumerate(iterable):
        if i:
            yield delimiter
        yield v
# ----------------------------------------
def annual_return(start, percent, years):
    return (start * (1 + percent / 100)**year for year in range(1, years + 1))
# ----------------------------------------
def pluck(data, path, default=None):
    try:
        for i in path.split('.'):
            data = data.get(i, default)
    except AttributeError:
        return default
    return data
# ----------------------------------------
import functools
def recviz(func):
    left = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal left
        args_ = list(map(repr, args))
        kwargs_ = [f'{k}={repr(v)}' for k, v in kwargs.items()]
#       kwargs_ = [f'{k}={v!r}' for k, v in kwargs.items()]
        print(f'{[" " * left, left := left + 4][0]}-> {func.__name__}({", ".join(args_ + kwargs_)})')
        value = func(*args, **kwargs)
        print(f'{[left := left - 4, " " * left][1]}<- {repr(value)}')
#       print(f'{[left := left - 4, " " * left][1]}<- {value!r}')
        return value
    return wrapper
# ======================================== 4.1
class PiggyBank:
    pass
money_box = PiggyBank()
# ----------------------------------------
class PiggyBank:
    pass
money_box1 = PiggyBank()
money_box2 = PiggyBank()
money_box1.coins = 10
money_box2.coins = 15
money_box2.color = 'pink'
# ----------------------------------------
class PiggyBank:
    content = 'coins'
    alternate_name = 'penny bank'
money_box = PiggyBank()
# ======================================== 4.3
class Gun:
    def shoot(self):
        print('pif')
# ----------------------------------------
class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n
# ----------------------------------------
class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color):
        self.color = new_color
        
    def add_rooms(self, n):
        self.rooms += n
# ----------------------------------------
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * self.radius**2
# ----------------------------------------
class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n
# ----------------------------------------
from itertools import cycle
class Gun:
    def __init__(self):
        self.shot = cycle(['pif', 'paf'])

    def shoot(self):
        print(next(self.shot))
# ----------------------------------------
from itertools import cycle
class Gun:
    def __init__(self):
        self.shot = cycle(['pif', 'paf'])
        self.shot_count = 0

    def shoot(self):
        print(next(self.shot))
        self.shot_count += 1

    def shots_count(self):
        return self.shot_count

    def shots_reset(self):
        self.shot_count = 0
        self.shot = cycle(['pif', 'paf'])
# ----------------------------------------
class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n

    def get_result(self):
        if self.right > self.left:
            return 'Правая чаша тяжелее'
        elif self.right < self.left:
            return 'Левая чаша тяжелее'
        else:
            return 'Весы в равновесии'
# ----------------------------------------
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x**2 + self.y**2)**0.5
# ----------------------------------------
class Numbers:
    def __init__(self):
        self.list_ = []

    def add_number(self, n):
        self.list_.append(n)

    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.list_))

    def get_odd(self):
        return list(filter(lambda x: x % 2 == 1, self.list_))
# ----------------------------------------
class TextHandler:
    def __init__(self):
        self.list_ = []

    def add_words(self, text):
        self.list_.extend(text.split())

    def get_shortest_words(self):
        if not self.list_:
            return []
        min_ = min(map(len, self.list_))
        return list(filter(lambda x: len(x) == min_, self.list_))

    def get_longest_words(self):
        if not self.list_:
            return []
        max_ = max(map(len, self.list_))
        return list(filter(lambda x: len(x) == max_, self.list_))
# ----------------------------------------
class Todo:
    def __init__(self):
        self.things = []

    def add(self, name, priority):
        self.things.append((name, priority))

    def get_by_priority(self, priority):
        if not self.things:
            return []
        return [n for n, p in self.things if p == priority]

    def get_low_priority(self):
        if not self.things:
            return []
        min_ = min(p for n, p in self.things)
        return [n for n, p in self.things if p == min_]

    def get_high_priority(self):
        if not self.things:
            return []
        max_ = max(p for n, p in self.things)
        return [n for n, p in self.things if p == max_]


class Todo:
    def __init__(self):
        self.things = []

    def add(self, thing, priority):
        self.things.append((thing, priority))

    def get_by_priority(self, priority):
        return [t for t, p in self.things if p == priority]

    def get_low_priority(self):
        priority = min(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)

    def get_high_priority(self):
        priority = max(map(lambda t: t[1], self.things)) if self.things else None
        return self.get_by_priority(priority)
# ----------------------------------------
class Postman:
    def __init__(self):
        self.delivery_data = []

    def del_duplicate(self, list_):
        l = []
        for e in list_:
            if e not in l:
                l.append(e)
        return l

#   def del_duplicate(self, list_):
#       dict_keys = {}.fromkeys(list_)
#       return list(dict_keys.keys())        

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        return self.del_duplicate(
            [h for s, h, f in self.delivery_data if s == street] if self.delivery_data else [])

    def get_flats_for_house(self, street, house):
        return self.del_duplicate(
            [f for s, h, f in self.delivery_data if s == street and h == house] if self.delivery_data else [])
# ----------------------------------------
from copy import copy
class Wordplay:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = copy(words)
#       self.words = copy(words if words else [])

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n):
        return [w for w in self.words if len(w) == n] if self.words else []

    def only(self, *args):
        return [w for w in self.words if set(w) <= set(args)] if self.words else []

    def avoid(self, *args):
        return [w for w in self.words if set(w) & set(args) == set()] if self.words else []


class Wordplay:
    def __init__(self, words=()):
        self.words = []
        self.words.extend(words)
        
    def add_word(self, word):
        self.words.append(word)
        
    def words_with_length(self, n):
        return [w for w in self.words if len(w) == n]
    
    def only(self, *args):
        return [w for w in self.words if set(w) <= set(args)]

    def avoid(self, *args):
        return [w for w in self.words if len(set(w) & set(args)) == 0]
# ----------------------------------------
class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.h_range = 'abcdefgh'

    def get_char(self):
        return 'N'

    def can_move(self, h, v):
        if ((abs(self.h_range.index(h) - self.h_range.index(self.horizontal)) == 2 and abs(v - self.vertical) == 1)
                    or (abs(self.h_range.index(h) - self.h_range.index(self.horizontal)) == 1 and abs(v - self.vertical) == 2)):
            return True
        return False

#   def can_move(self, col, row):
#       return (ord(self.col) - ord(col))**2 + (self.row - row)**2 == 5

    def move_to(self, h, v):
        if self.can_move(h, v):
            self.horizontal = h
            self.vertical = v

    def draw_board(self):
        for v in range(8, 0, -1):
            for h in self.h_range:
                if self.horizontal == h and self.vertical == v:
                    print(self.get_char(), end='')
                elif self.can_move(h, v):
                    print('*', end='')
                else:
                    print('.', end='')
            print()
# ======================================== 4.4
from math import pi
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * radius ** 2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area
# ----------------------------------------
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError('На счете недостаточно средств')

    def transfer(self, account, amount):
        if amount <= self._balance:
            self._balance -= amount
            account.deposit(amount)
        else:
            raise ValueError('На счете недостаточно средств')
# ----------------------------------------
class User:
    def __init__(self, name, age):
        self._name = self.check_name(name)
        self._age = self.check_age(age)

    @staticmethod
    def check_name(name):
        if isinstance(name, str) and name.isalpha():
            return name
        else:
            raise ValueError('Некорректное имя')

    @staticmethod
    def check_age(age):
        if isinstance(age, int) and age in range(111):
            return age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = self.check_name(new_name)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = self.check_age(new_age)


class User:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if not (isinstance(new_name, str) and new_name.isalpha() and new_name):
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if not (isinstance(new_age, int) and (0 <= new_age <= 110)):
            raise ValueError('Некорректный возраст')
        self._age = new_age
# ======================================== 4.5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)
# ----------------------------------------
class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if not (isinstance(hours, int) and (1 <= hours <= 12)):
            raise ValueError('Некорректное время')
        self._hours = hours

    hours = property(get_hours, set_hours)
# ----------------------------------------
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return self.name + ' ' + self.surname

    def set_fullname(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)
# ======================================== 4.6
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @property
    def fullname(self):
        return self.name + ' ' + self.surname

    @fullname.setter
    def fullname(self, fullname):
        self.name, self.surname = fullname.split()
# ----------------------------------------
def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
         hash_value += ord(char) * index
    return hash_value % 10**9

class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password
#       self._password = hash_function(password)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_function(password)
# ----------------------------------------
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discr(self):
        return self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        return (- self.b - self.discr() ** 0.5) / (2 * self.a) if self.discr() >= 0 else None

    @property
    def x2(self):
        return (- self.b + self.discr() ** 0.5) / (2 * self.a) if self.discr() >= 0 else None

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, args):
        self.a, self.b, self.c = args
# ----------------------------------------
class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, hexcode):
        self._hexcode = hexcode
        self.r = int(hexcode[:2], base=16)
        self.g = int(hexcode[2:4], base=16)
        self.b = int(hexcode[4:], base=16)
# ======================================== 4.7
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
# ----------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side, side)
# ----------------------------------------
class QuadraticPolynomial:
    def __init__(self, *args):
        self.a, self.b, self.c = args

    @classmethod
    def from_iterable(cls, args):
        return cls(*args)

    @classmethod
    def from_str(cls, string):
        return cls(*map(float, string.split()))
#       return cls.from_iterable(map(float, s.split()))
# ----------------------------------------
class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        self.pets.append(self)
#       Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        return cls.pets[0] if cls.pets else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if cls.pets else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)
# ----------------------------------------
class StrExtension:
    @staticmethod
    def remove_vowels(string):
        return ''.join(filter(lambda x: x not in 'aeiouyAEIOUY', string))
        # return string.translate(str.maketrans('', '', 'aeiouyAEIOUY'))  # delete 'aeiouyAEIOUY'

    @staticmethod
    def leave_alpha(string):
        return ''.join(filter(lambda x: x in ascii_letters, string))

    @staticmethod
    def replace_all(string, chars, char):
        if not char:
            return string.translate(str.maketrans('', '', chars))  # delete chars
        return string.translate(str.maketrans(chars, char * len(chars)))  # '123' -> 'abc'


class StrExtension:
    __VOWELS = re.compile(r'[aeiouy]', flags=re.I)
    __ALPHABET = re.compile(r'[^a-zA-Z]')

    @staticmethod
    def remove_vowels(string):
        return StrExtension.__VOWELS.sub('', string)

    @staticmethod
    def leave_alpha(string):
        return StrExtension.__ALPHABET.sub('', string)

    @staticmethod
    def replace_all(string, chars, char):
        return re.sub(fr'[{chars}]', char, string)


class StrExtension:
    @staticmethod
    def remove_vowels(string):
        return ''.join(i for i in string if i.lower() not in 'aeiouy')
    
    @staticmethod
    def leave_alpha(string):
        return ''.join(i for i in string if i.isalpha())
    
    @staticmethod
    def replace_all(string, chars, char):
        return ''.join(char if i in chars else i for i in string)
# ----------------------------------------
import re
class CaseHelper:
    @staticmethod
    def is_snake(string):
        return bool(re.fullmatch(r'^[a-z]+(_[a-z]+)*$', string))

    @staticmethod
    def is_upper_camel(string):
        return bool(re.fullmatch(r'^([A-Z][a-z]*)+$', string))

    @staticmethod
    def to_snake(string):
        return re.sub(r'([A-Z])', r'_\1', string).lower()[1:]

    @staticmethod
    def to_upper_camel(string):
        return re.sub(r'_', r'', string.title())
#       return string.title().replace('_', '')
# ======================================== 4.8
from functools import singledispatchmethod
class Processor:
    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def _from_int_float(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def _from_str(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def _from_list(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def _from_tuple(data):
        return tuple(sorted(data))
# ----------------------------------------
from functools import singledispatchmethod
class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _from_int_float(data):
        return - data

    @neg.register(bool)
    @staticmethod
    def _from_bool(data):
        return not data
# ----------------------------------------
from functools import singledispatchmethod
class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def _from_int(data):
        print('Целое число:', data)

    @format.register(float)
    @staticmethod
    def _from_float(data):
        print('Вещественное число:', data)

    @format.register(list)
    @staticmethod
    def _from_list(data):
        print('Элементы списка: ', end='')
        print(*data, sep=', ')
#       print(f'Элементы списка: {str(data)[1:-1]}')
#       print('Элементы списка:', ', '.join(map(str, obj)))

    @format.register(tuple)
    @staticmethod
    def _from_tuple(data):
        print('Элементы кортежа: ', end='')
        print(*data, sep=', ')
#       print(f'Элементы кортежа: {str(data)[1:-1]}')
#       print('Элементы кортежа:', ', '.join(map(str, obj)))

    @format.register(dict)
    @staticmethod
    def _from_dict(data):
        print('Пары словаря: ', end='')
        print(*((k, v) for k, v in data.items()), sep=', ')
#       print(f'Пары словаря: {str(data.items())[12:-2]}')
#       print('Пары словаря:', ', '.join(map(str, obj.items())))
# ----------------------------------------
from datetime import date
from dateutil.relativedelta import relativedelta
from functools import singledispatchmethod
class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _from_str(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_tuple(self, birth_date):
        try:
            self.birth_date = date(*birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        return relativedelta(date.today(), self.birth_date).years
# ======================================== 5.1
class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # при первом вызове создаем объект
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'
# ======================================== 5.2
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
# ----------------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'
# ----------------------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор на плоскости с координатами ({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
# ----------------------------------------
from functools import singledispatchmethod
class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    @__init__.register(list)
    @__init__.register(tuple)
    def _from_list_tuple(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))

    def __str__(self):
        return f'{self.ipaddress}'

    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"
#       return f"{self.__class__.__name__}('{self.ipaddress}')"
# ----------------------------------------
class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number.replace(' ', '')

    def __str__(self):
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.phone_number}')"
# ----------------------------------------
class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            exec(f"self.{k} = {repr(v)}")
#           setattr(self, k, v)

    def __str__(self):
        kwargs_ = ', '.join([f'{k}={repr(v)}' for k, v in self.__dict__.items()])
        return f"AnyClass: {kwargs_}"

    def __repr__(self):
        kwargs_ = ', '.join([f'{k}={repr(v)}' for k, v in self.__dict__.items()])
        return f"AnyClass({kwargs_})"


class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'AnyClass: {", ".join(self._attrs())}'

    def __repr__(self):
        return f'AnyClass({", ".join(self._attrs())})'

    def _attrs(self):
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]
# ======================================== 5.3
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        return NotImplemented
# ----------------------------------------
from functools import total_ordering
@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word.title()

    def __repr__(self):
        return f"Word('{self.word}')"

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented
# ----------------------------------------
from functools import total_ordering
@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    @staticmethod
    def year_month(year, month):
        return f'{year}{month:02}'

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year_month(self.year, self.month) == self.year_month(other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year_month(self.year, self.month) == self.year_month(other[0], other[1])) if len(other) == 2 else NotImplemented
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return self.year_month(self.year, self.month) < self.year_month(other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year_month(self.year, self.month) < self.year_month(other[0], other[1])) if len(other) == 2 else NotImplemented
        return NotImplemented


from functools import total_ordering
@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __eq__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) == (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) == other
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year, self.month) < other
        return NotImplemented
# ----------------------------------------
from functools import total_ordering
@total_ordering
class Version:
    def __init__(self, version):
        self.version = '.'.join((version.split('.') + ['0', '0'])[:3])

    def __str__(self):
        return f"{self.version}"

    def __repr__(self):
        return f"Version('{self.version}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return [int(i) for i in self.version.split('.')] == [int(i) for i in other.version.split('.')]
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return [int(i) for i in self.version.split('.')] < [int(i) for i in other.version.split('.')]
        return NotImplemented


from functools import total_ordering
@total_ordering
class Version:
    def __init__(self, version):
        self._parts = [int(i) for i in version.split('.')]
        self._parts += [0] * (3 - len(self._parts))

    def __str__(self):
        return '{}.{}.{}'.format(*self._parts)
    
    def __repr__(self):
        return "Version('{}.{}.{}')".format(*self._parts)
    
    def __eq__(self, other):
        if isinstance(other, Version):
            return self._parts == other._parts
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Version):
            return self._parts < other._parts
        return NotImplemented
# ======================================== 5.4
class ReversibleString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __neg__(self):
        return ReversibleString(self.string[::-1])
#       return self.__class__(self.string[::-1])
# ----------------------------------------
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{self.amount} руб.'

    def __pos__(self):
        return Money(abs(self.amount))

    def __neg__(self):
        return Money(-abs(self.amount))
# ----------------------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
# ----------------------------------------
import numpy as np
class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'ColoredPoint({self.x}, {self.y}, {self.color})'

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)

    def __invert__(self):
        return ColoredPoint(self.y, self.x, tuple(np.array((255, 255, 255)) - np.array(self.color)))
#       return ColoredPoint(self.y, self.x, tuple(255 - c for c in self.color))
# ----------------------------------------
import re
import numpy as np
from functools import singledispatch
class Matrix:
    @singledispatch
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.matrix = np.full((self.rows, self.cols), value, dtype=float)

    def get_value(self, row, col):
        value = self.matrix[row, col]
        return int(value) if value == round(value) else value

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __str__(self):
        string = '\n'.join([' '.join(map(str, i)) for i in self.matrix])
        return re.sub(r'(\.0)\b', r'', string)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.matrix = self.matrix
        return new_matrix

    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.matrix = -self.matrix
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows)
        new_matrix.matrix = self.matrix.T
        return new_matrix

    def __round__(self, n=0):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.matrix = self.matrix.round(n)
        return new_matrix


class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def _create_matrix_instance(self, rows, cols, sign=1, do_transpose=False, do_round=False, n=None):
        matrix = Matrix(rows, cols)
        for row in range(rows):
            for col in range(cols):
                r, c = (col, row) * do_transpose or (row, col)
                value = round(self.get_value(r, c) * sign, n) * do_round or self.get_value(r, c) * sign
                matrix.set_value(row, col, value)
        return matrix

    def __str__(self):
        string_matrix = [' '.join(map(str, item)) for item in self.matrix]
        return '\n'.join(string_matrix)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        return self._create_matrix_instance(self.rows, self.cols)

    def __neg__(self):
        return self._create_matrix_instance(self.rows, self.cols, sign=-1)

    def __invert__(self):
        return self._create_matrix_instance(self.cols, self.rows, do_transpose=True)

    def __round__(self, n=None):
        return self._create_matrix_instance(self.rows, self.cols, do_round=True, n=n)
# ======================================== 5.5
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, int | float):
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented
# ----------------------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return __class__(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return __class__(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x / other, self.y / other)
        return NotImplemented
# ----------------------------------------
class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'{self.string}'

    def __repr__(self):
        return f'{__class__}({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, SuperString):
            return __class__(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return __class__(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return __class__(self.string[:len(self.string) // other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            return __class__(self.string[:-other if other else len(self.string)])
#           return __class__(self.string[:-other or None])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return __class__(self.string[other:])
        return NotImplemented
# ----------------------------------------
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours % 24 + minutes // 60
        self.minutes = minutes % 60

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}'

    def __add__(self, other):
        if isinstance(other, Time):
            hours = (self.hours + other.hours) % 24 + (self.minutes + other.minutes) // 60
            minutes = (self.minutes + other.minutes) % 60
            return __class__(hours, minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours = (self.hours + other.hours) % 24 + (self.minutes + other.minutes) // 60
            self.minutes = (self.minutes + other.minutes) % 60
            return self
        return NotImplemented
# ----------------------------------------
class Queue:
    def __init__(self, *args):
        self.line = [*args]

    def add(self, *args):
        self.line.extend(args)

    def pop(self):
        return self.line.pop(0) if self.line else None

    def __str__(self):
        return ' -> '.join(str(i) for i in self.line)

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.line == other.line
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            self.line.extend(other.line)
            return __class__(*self.line)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.line.extend(other.line)
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return __class__(*self.line[other:])
        return NotImplemented
# ======================================== 5.6
class Calculator:
    def __call__(self, a, b, operation):
        try:
            return eval(f'{a}{operation}{b}')
        except ZeroDivisionError:
            raise ValueError('Деление на ноль невозможно')
# ----------------------------------------
class RaiseTo:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x):
        return x**self.degree
# ----------------------------------------
import random
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return random.randint(1, self.sides)
# ----------------------------------------
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x**2 + self.b * x + self.c
# ----------------------------------------
class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return string.strip(self.chars)
# ----------------------------------------
class Filter:
    def __init__(self, predicate=None):
        self.predicate = predicate

    def __call__(self, iterable):
        return [*filter(self.predicate, iterable)]
# ----------------------------------------
from datetime import date
class DateFormatter:
    __COUNTRY_CODES = {
        'ru': '%d.%m.%Y',
        'fr': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'pt': '%d-%m-%Y'
    }

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d):
        return d.strftime(self.__COUNTRY_CODES[self.country_code])
# ----------------------------------------
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.func(*args, **kwargs)
# ----------------------------------------
class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        result = self.cache.get((*args, *kwargs.values()))
        if result is None:
            result = self.func(*args, **kwargs)
            self.cache[(*args, *kwargs.values())] = result
        return result


class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        result = self.cache.get(args) or self.func(*args)
        self.cache.setdefault(args, result)
        return result
# ----------------------------------------
class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, x):
        return eval(', '.join([f'x.{arg}' for arg in self.args]))


class SortKey:
    def __init__(self, *attributes):
        self.attributes = attributes

    def __call__(self, instance):
        return [getattr(instance, attribute) for attribute in self.attributes]


from operator import attrgetter as SortKey


# example
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))  # SortKey('name')(User('Gvido', 67)) - 1-st call
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))
# ======================================== 5.7
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return False if self.x == self.y == 0 else True

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __int__(self):
        return int(self.abs())

    def __float__(self):
        return self.abs()

    def __complex__(self):
        return complex(self.x, self.y)
# ----------------------------------------
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f'{round(self.temperature, 2)}°C'
    
    def to_fahrenheit(self):
        return 32 + 1.8 * self.temperature

    @classmethod
    def from_fahrenheit(cls, temperature):
        return cls((temperature - 32) * 5 / 9)

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return self.temperature
# ----------------------------------------
from roman import toRoman, fromRoman
from functools import total_ordering
@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        return fromRoman(self.number)

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return fromRoman(self.number) == fromRoman(other.number)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return fromRoman(self.number) < fromRoman(other.number)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return __class__(toRoman(fromRoman(self.number) + fromRoman(other.number)))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return __class__(toRoman(fromRoman(self.number) - fromRoman(other.number)))
        return NotImplemented


from functools import total_ordering
@total_ordering
class RomanNumeral:
    @staticmethod
    def to_roman(number):
        # Storing roman values of digits from 0-9
        # when placed at different places
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
             "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
             "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
             "VI", "VII", "VIII", "IX"]
        # Converting to roman
        thousands = m[number // 1000]
        hundreds = c[(number % 1000) // 100]
        tens = x[(number % 100) // 10]
        ones = i[number % 10]
        ans = (thousands + hundreds +
               tens + ones)
        return ans.replace(' ', '')

    @staticmethod
    def from_roman(number):
        dict_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dict_str = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
        list_ = list(number)
        for i in range(len(list_) - 1):
            list_[i] = (f'-{list_[i]}' if dict_int[list_[i]] < dict_int[list_[i + 1]] else f'+{list_[i]}')
        list_[-1] = f'+{list_[-1]}'
        return eval(''.join(list_).translate(str.maketrans(dict_str)))

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        return self.from_roman(self.number)

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.from_roman(self.number) == self.from_roman(other.number)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.from_roman(self.number) < self.from_roman(other.number)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return __class__(self.to_roman(self.from_roman(self.number) + self.from_roman(other.number)))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return __class__(self.to_roman(self.from_roman(self.number) - self.from_roman(other.number)))
        return NotImplemented
# ======================================== 5.8
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return self.price * self.quantity
        elif name == 'name':
            return object.__getattribute__(self, name).title()
        return object.__getattribute__(self, name)
# ----------------------------------------
class Logger:
    def __setattr__(self, name, value):
        print(f'Изменение значения атрибута {name} на {value}')
        self.__dict__[name] = value

    def __delattr__(self, name):
        print(f'Удаление атрибута {name}')
        del self.__dict__[name]
# ----------------------------------------
class Ord:
    def __getattr__(self, name):
        return ord(name)
# ----------------------------------------
class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        return self.default
# ----------------------------------------
class NonNegativeObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattribute__(self, item):
        if isinstance(object.__getattribute__(self, item), int | float):
            return abs(object.__getattribute__(self, item))
        return object.__getattribute__(self, item)


class NonNegativeObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        
    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, name, value)
# ----------------------------------------
from copy import copy
class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = len(kwargs)
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        d = copy(self.__dict__)
        self.__dict__[key] = value
        if key not in d:
            self.attrs_num += 1

    def __delattr__(self, item):
        del self.__dict__[item]
        self.attrs_num -= 1


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __getattr__(self, name):
        if name == 'attrs_num':
            return len(self.__dict__) + 1


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    @property
    def attrs_num(self):
        return len(self.__dict__) + 1


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 0
        for i, j in kwargs.items():
            setattr(self, i, j)
            
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        object.__setattr__(self, 'attrs_num', (self.attrs_num + 1))
        
    def __delattr__(self, name):
        object.__setattr__(self, 'attrs_num', (self.attrs_num - 1))
        object.__delattr__(self, name)
# ----------------------------------------
class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        self.__dict__[key] = value
#       object.__setattr__(self, key, value)

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')
# ----------------------------------------
class ProtectedObject:
    def __init__(self, **kwargs):
        self.is_locked = False
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.is_locked = True

    def __getattribute__(self, item):
        if object.__getattribute__(self, 'is_locked') and item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'is_locked':
            object.__setattr__(self, key, value)
        elif self.is_locked and key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if self.is_locked and item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, item)


class ProtectedObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)
        
    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, name)
        
    def __setattr__(self, name, value):
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__setattr__(self, name, value)
        
    def __delattr__(self, name):
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, name)


class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            super().__setattr__(key, value)

    @staticmethod
    def check_protected(name):
        if name.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
            
    def __getattribute__(self, name):
        super().__getattribute__('check_protected')(name)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        self.check_protected(name)
        super().__setattr__(name, value)

    def __delattr__(self, name):
        self.check_protected(name)
        super().__delattr__(name)
# ======================================== 5.9
def hash_function(obj):
    obj = str(obj)
    start, end = 0, len(obj) - 1
    temp1 = 0
    while start < end:
        temp1 += ord(obj[start]) * ord(obj[end])
        start += 1
        end -= 1
    if len(obj) % 2:
        temp1 += ord(obj[int(len(obj) // 2)])
    temp2 = sum((-1)**(i + 1) * i * ord(j) for i, j in enumerate(obj, start=1))
    return (temp1 * temp2) % 123456791


def hash_function(obj):
    obj = str(obj)
    temp1 = temp2 = 0
    for i in range(len(obj) // 2):
        temp1 += ord(obj[i]) * ord(obj[-(i + 1)])
    if len(obj) % 2:
        temp1 += ord(obj[len(obj) // 2])
    for i, c in enumerate(obj, 1):
        temp2 += ord(c) * i * ((-1) ** (i + 1))
    return temp1 * temp2 % 123456791
# ----------------------------------------
def limited_hash(left, right, hash_function=hash):
    def func(obj):
        return left + (hash_function(obj) - left) % (right - left + 1)
    return func
# ======================================== 5.10
class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x == other.x
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))
# ----------------------------------------
class Row:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        else:
            raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, item):
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self):
        kwargs_ = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f'Row({", ".join(kwargs_)})'

    def __eq__(self, other):
        if isinstance(other, Row):
            return tuple(self.__dict__.items()) == tuple(other.__dict__.items())
        return NotImplemented

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))
# ======================================== 6.1
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Point({self.x}, {self.y}, {self.z})'

    def __iter__(self):
        yield from (self.x, self.y, self.z)
# ----------------------------------------
class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self, *args):
        self.junior.extend(args)

    def add_senior(self, *args):
        self.senior.extend(args)

    def __iter__(self):
        yield from ((i, 'junior') for i in self.junior)
        yield from ((i, 'senior') for i in self.senior)
#       for junior in self._juniors:
#           yield (junior, 'junior')
#       for senior in self._seniors:
#           yield (senior, 'senior')


class DevelopmentTeam:
    def __init__(self):
        self.__juniors = []
        self.__seniors = []

    def add_junior(self, *names):
        self.__juniors.extend((name, 'junior') for name in names)

    def add_senior(self, *names):
        self.__seniors.extend((name, 'senior') for name in names)

    def __iter__(self):
        yield from it.chain(self.__juniors, self.__seniors)
# ----------------------------------------
class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj
        self.keys = iter(obj.__dict__)

    def __iter__(self):
        return self

    def __next__(self):
        key = next(self.keys)
        return (key, self.obj.__dict__[key])


class AttrsIterator:
    def __init__(self, obj):
        self.iterator = iter(obj.__dict__.items())
        
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.iterator)


class AttrsIterator:
    def __new__(cls, obj):
        return iter(obj.__dict__.items())
# ----------------------------------------
class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterable)
        try:
            for _ in range(self.n):
                next(self.iterable)
        except StopIteration:
            pass
        return value
# ----------------------------------------
from itertools import chain
import random
class RandomLooper:
    def __init__(self, *args):
        list_ = list(chain(*args))
        random.shuffle(list_)
        self.iterator = iter(list_)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)
# ----------------------------------------
from copy import deepcopy
class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.iterator_peek = iter(deepcopy(iterable))
        self.get_next_peek()

    def get_next_peek(self):
        try:
            self.next_peek = next(self.iterator_peek)
        except:
            self.next_peek = StopIteration

    def peek(self, default=StopIteration):
        if self.next_peek == StopIteration:
            if default == StopIteration:
                raise StopIteration
            else:
                return default
        return self.next_peek

    def __iter__(self):
        return self

    def __next__(self):
        self.get_next_peek()
        return next(self.iterator)


SENTINEL = object()
class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.cache = []
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.peek()
        return self.cache.pop()
    
    def peek(self, default=SENTINEL):
        if not self.cache:
            try:
                self.cache.append(next(self.iterator))
            except StopIteration:
                if default is not SENTINEL:
                    return default
                raise
        return self.cache[0]
# ----------------------------------------
from copy import deepcopy
class LoopTracker:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.iterator_copy = iter(deepcopy(iterable))
        self._accesses = 0
        self._empty_accesses = 0
        self._last = SystemError
        self._is_empty = False
        try:
            self._first = next(self.iterator_copy)
        except:
            self._first = StopIteration

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first == StopIteration:
            raise AttributeError('Исходный итерируемый объект пуст')
        else:
            return self._first

    @property
    def last(self):
        if self._last == SystemError:
            raise AttributeError('Последнего элемента нет')
        else:
            return self._last

    def is_empty(self):
        return self._is_empty

    def __iter__(self):
        return self

    def __next__(self):
        try:
            next(self.iterator_copy)
        except:
            self._is_empty = True
        try:
            self._last = next(self.iterator)
            self._accesses += 1
            return self._last
        except:
            self._empty_accesses += 1
            self._last = StopIteration
            raise StopIteration
# ======================================== 6.2
class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[len(self.sequence) - key - 1]
#       return self.sequence[len(self) - key - 1]
#       return self.sequence[~key]

    def __iter__(self):
        yield from reversed(self.sequence)
# ----------------------------------------
class SparseArray:
    def __init__(self, default):
        self.default = default
        self.array = {}

    def __len__(self):
        return len(self.array)

    def __getitem__(self, key):
        return self.array.get(key, self.default)

    def __setitem__(self, key, value):
        self.array[key] = value
# ----------------------------------------
class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.cyclic_list = list(iterable)
        self.next_ind = -1

    def append(self, obj):
        self.cyclic_list.append(obj)

    def pop(self, n=-1):
        return self.cyclic_list.pop(n)

    def __len__(self):
        return len(self.cyclic_list)

    def __getitem__(self, key):
        return self.cyclic_list[key % len(self)]

    def __iter__(self):
        return self

    def __next__(self):
        self.next_ind += 1
        return self.cyclic_list[self.next_ind % len(self)]


from itertools import cycle
class CyclicList:
    def __init__(self, iterable=()):
        self._data = list(iterable) or []

    def append(self, item):
        self._data.append(item)

    def pop(self, index=None):
        if index is None:
            return self._data.pop()
        return self._data.pop(index)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from cycle(self._data)

    def __getitem__(self, index):
        return self._data[index % len(self._data)]
# ----------------------------------------
from copy import deepcopy
class SequenceZip:
    def __init__(self, *args):
        self.args = deepcopy(args)

    def __len__(self):
        return min((len(arg) for arg in self.args), default=0)

    def __getitem__(self, key):
        data = zip(*self.args)
        for _ in range(key):
            next(data)
        return next(data)

    def __iter__(self):
        return zip(*self.args)

    def __next__(self):
        return next(zip(*self.args))


import copy
class SequenceZip:
    def __init__(self, *iterables):
        self.iterables = copy.deepcopy(iterables)

    def __len__(self):
        return min((len(s) for s in self.iterables), default=0)

    def __getitem__(self, index):
        return tuple(s[index] for s in self.iterables)

    def __iter__(self):
        yield from zip(*self.iterables)
# ----------------------------------------
class OrderedSet:
    def __init__(self, iterable=None):
        self.ord_set = dict.fromkeys(iterable) if iterable else dict()

    def add(self, obj):
        self.ord_set.update({obj: None})

    def discard(self, obj):
        if obj in self.ord_set:
            del self.ord_set[obj]

    def __len__(self):
        return len(self.ord_set)

    def __contains__(self, item):
        return item in self.ord_set

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return tuple(self.ord_set) == tuple(other.ord_set)
        elif isinstance(other, set):
            return set(self.ord_set) == other
        return NotImplemented

    def __iter__(self):
        return iter(self.ord_set)


class OrderedSet:
    def __init__(self, iterable=()):
        self._data = dict.fromkeys(iterable, None)

    def __len__(self):
        return len(self._data)

    def add(self, item):
        self._data.setdefault(item, None)

    def discard(self, item):
        self._data.pop(item, None)

    def __iter__(self):
        yield from self._data

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self._data) == len(other._data) and all(x == y for x, y in zip(self._data, other._data))
        if isinstance(other, set):
            return set(self._data) == other
        return NotImplemented
# ----------------------------------------
from copy import deepcopy
class AttrDict:
    def __init__(self, data=()):
        self._data = deepcopy(data) or dict()
#       self._data = dict(data) or {}

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __iter__(self):
        yield from self._data

    def __getattr__(self, item):
        return self.__getitem__(item)
#       return self._data[key]
# ----------------------------------------
class PermaDict:
    def __init__(self, data=()):
        self._data = dict(data) or dict()

    def keys(self):
        yield from self._data.keys()

    def values(self):
        yield from self._data.values()

    def items(self):
        yield from self._data.items()

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if key in self._data:
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        yield from self._data
# ----------------------------------------
from collections import defaultdict
class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self._data = defaultdict(list)
        for key, value in data.items():
            self._data[key].append(value)

    def keys(self):
        yield from self._data.keys()

    def values(self):
        yield from (value[-1] for value in self._data.values())

    def items(self):
        yield from ((key, value[-1]) for key, value in self._data.items())

    def history(self, key):
        value = self._data[key]
        if not value:
            del self._data[key]
        return value

    def all_history(self):
        return dict(self._data)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data

    def __getitem__(self, key):
        return self._data[key][-1]

    def __setitem__(self, key, value):
        self._data[key].append(value)

    def __delitem__(self, key):
        del self._data[key]


class HistoryDict:
    def __init__(self, data=()):
        self._data = dict(data) or {}
        self._history = {key: [value] for key, value in self._data.items()}

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self.keys())

    def __delitem__(self, key):
        del self._data[key]
        del self._history[key]

    def __setitem__(self, key, value):
        self._history.setdefault(key, []).append(value)
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]
# ----------------------------------------
class MutableString:
    def __init__(self, string=''):
        self._string = list(string)

    def lower(self):
        self._string = ''.join(self._string).lower()

    def upper(self):
        self._string = ''.join(self._string).upper()

    def __str__(self):
        return ''.join(self._string)

    def __repr__(self):
        return f"MutableString('{''.join(self._string)}')"

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        yield from self._string

    def __getitem__(self, key):
        if isinstance(key, slice):
            return MutableString(''.join(self._string[key]))
        if isinstance(key, int):
            return self._string[key]

    def __setitem__(self, key, value):
        self._string[key] = value
        self._string = list(''.join(self._string))

    def __delitem__(self, key):
        del self._string[key]

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(''.join(self._string + other._string))
        return NotImplemented
# ----------------------------------------
from collections import defaultdict
class Grouper:
    def __init__(self, iterable, key):
        self._data = defaultdict(list)
        self.key = key
        for value in iterable:
            self._data[self.key(value)].append(value)

    def add(self, obj):
        self._data[self.key(obj)].append(obj)

    def group_for(self, obj):
        return self.key(obj)

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        yield from self._data.items()

    def __getitem__(self, key):
        return self._data[key]

    def __contains__(self, item):
        return item in self._data
# ======================================== 6.3
def print_file_content(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('Файл не найден')
# ----------------------------------------
def non_closed_files(files):
    return filter(lambda x: not x.closed, files)
# ----------------------------------------
def log_for(logfile, date_str):
    with (
        open(logfile, 'r', encoding='utf-8') as file_from,
        open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as file_to
    ):
        for line in file_from.readlines():
            if line.startswith(f'{date_str}'):
                file_to.write(line[len(date_str) + 1:])
# ======================================== 6.4
def is_context_manager(obj):
    return '__enter__' in dir(obj) and '__exit__' in dir(obj)
# ======================================== 6.5
class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return True
# ----------------------------------------
class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'До встречи, {self.name}!')
# ----------------------------------------
class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.obj.close()
        except:
            print('Незакрываемый объект')
            return True
# ----------------------------------------
class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, mode='r', encoding='utf-8')
        return self.file.read().split('\n')
#       return (line.strip() for line in self.file)  # generator!

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, mode = 'r', encoding='utf-8')
        return self
    
    def __exit__(self, *args, **kwargs):
        self.file.close()
            
    def __iter__(self):
        for line in self.file:
            yield line.strip('\n')
# ----------------------------------------
class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def __iter__(self):
        yield from self.file
        self.file.seek(0)


class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self.file.readlines()

    def __exit__(self, *args, **kwargs):
        self.file.close()


class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.file)
        except StopIteration:
            self.file.seek(0)
            raise
# ----------------------------------------
import sys
class UpperPrint:
    def decorator(self, func):
        def wrapper(*args, **kwargs):
            args = (i.upper() for i in args)
            kwargs = {k: v.upper() for k, v in kwargs.items()}
            return func(*args, **kwargs)
        return wrapper

    def __enter__(self):
        self.old_write = sys.stdout.write
        sys.stdout.write = self.decorator(sys.stdout.write)

    def __exit__(self, *args, **kwargs):
        sys.stdout.write = self.old_write


import sys
class UpperPrint:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper_write
        return self

    def upper_write(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write


import sys
class UpperPrint:
    def __enter__(self):
        self.w = sys.stdout.write
        sys.stdout.write = lambda t: self.w(t.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.w


old = print
print = lambda x: old(x.upper())
# ----------------------------------------
class Suppress:
    def __init__(self, *args):
        self.args = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.args:
            self.exception = exc_value
            return True
# ----------------------------------------
class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def write(self, text):
        try:
            self.file1.write(text)
            self.file2.write(text)
        except:
            raise ValueError('Файл закрыт или недоступен для записи')

    def close(self):
        if self.file1:
            self.file1.close()
        if self.file2:
            self.file2.close()

    def writable(self):
        try:
            if self.file1.writable() and self.file2.writable():
                return True
        except:
            pass
        return False

    def closed(self):
        try:
            if self.file1.closed and self.file2.closed:
                return True
        except:
            pass
        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close:
            self.close()
# ----------------------------------------
from copy import copy, deepcopy
class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.data_copy = (deepcopy if deep else copy)(data)

    def __enter__(self):
        return self.data

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            # reset to origin depending on deep
            self.data.clear()
            if isinstance(self.data, list):
                self.data.extend(self.data_copy)
#               self.data[:] = self.data_copy
            if isinstance(self.data, set | dict):
                self.data.update(self.data_copy)
        return True
# ----------------------------------------
from time import perf_counter
class AdvancedTimer:
    def __init__(self):
        self.runs = []
        self.last_run = None
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)
        self.min = min(self.runs)
        self.max = max(self.runs)
# ----------------------------------------
class HtmlTag:
    the_print = print
    def decorator(self, func):
        def wrapper(*args, **kwargs):
            args = (list(args))
            args.insert(0, '  ')
            return func(*args, **kwargs)
        return wrapper

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        global print
        self.origin_print = print
        if self.inline:
            print(f'<{self.tag}>', sep='', end='')
        else:
            print(f'<{self.tag}>', sep='')
            # print = lambda x: self.origin_print(f'  {x}')
            print = self.decorator(print)
        return self

    def print(self, text):
        global print
        if self.inline:
            tmp_print = print
            print = HtmlTag.the_print
#           print = __class__.the_print
            print(text, sep='', end='')
            print = tmp_print
        else:
            print(text, sep='')

    def __exit__(self, exc_type, exc_value, traceback):
        global print
        print = self.origin_print
        if self.inline:
            tmp_print = print
            print = HtmlTag.the_print
            print(f'</{self.tag}>', sep='')
            print = tmp_print
        else:
            print(f'</{self.tag}>', sep='')


class HtmlTag:
    INDENT = 2
    depth = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.depth = type(self).depth
        self.inline = inline
        self.end_char = '' if inline else '\n'

    def __enter__(self):
        print(' ' * type(self).INDENT * self.depth + f'<{self.tag}>', end=self.end_char)
        type(self).depth += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.inline:
            print(f'</{self.tag}>')
        else:
            print(' ' * type(self).INDENT * self.depth + f'</{self.tag}>')
        type(self).depth -= 1

    def print(self, txt):
        if self.inline:
            print(txt, end=self.end_char)
        else:
            print(' ' * type(self).INDENT * (self.depth + 1) + txt, end=self.end_char)


class HtmlTag:
    __level = 0
    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        self._end = "\n" * (not self.inline)

    def __enter__(self):
        print("  " * HtmlTag.__level + f"<{self.tag}>", end=self._end)
        HtmlTag.__level += 1
        return self

    def __exit__(self, *args, **kwargs):
        HtmlTag.__level -= 1
        print("  " * HtmlTag.__level  * (not self.inline) + f"</{self.tag}>")

    def print(self, value):
        print("  " * HtmlTag.__level * (not self.inline) + value, end=self._end)
# ----------------------------------------
class TreeBuilder:
    def __init__(self):
        self._tree = []

    def add(self, obj):
        self._tree.append(f'{repr(obj)}, ')
#       self._tree.extend([repr(obj), ', '])

    def structure(self):
        str_tree = '[' + ''.join(map(str, self._tree)) + ']'
        while '[]' in str_tree[1:-1]:
            str_tree = '[' + str_tree[1:-1].replace('[]', '') + ']'
        while ', , ' in str_tree:
            str_tree = str_tree.replace(', , ', ', ')
        str_tree = str_tree.replace(', ]', ']')
        str_tree = str_tree.replace('[, ', '[')
        return str_tree

    def __enter__(self):
        self._tree.append(', [')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._tree.append('], ')


class TreeBuilder:
    def __init__(self):
        self.knots = [[]]
        
    def __enter__(self):
        self.knots.append([])
        
    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])
        self.knots.pop()
    
    def add(self, value):
        self.knots[-1].append(value)
        
    def structure(self):
        return self.knots[-1]
# ======================================== 6.6
from contextlib import contextmanager
@contextmanager
def make_tag(tag):
    print(tag)
    yield
    print(tag)
# ----------------------------------------
import sys
from contextlib import contextmanager
@contextmanager
def reversed_print():
    standart_output = sys.stdout.write
    sys.stdout.write = lambda text: standart_output(''.join(reversed(text)))
#   sys.stdout.write = lambda text: standart_output(text[::-1])
    yield
    sys.stdout.write = standart_output
# ----------------------------------------
from contextlib import contextmanager
@contextmanager
def safe_write(filename):
    file = open(filename, mode='a', encoding='utf-8')
    cursor = file.tell()
    try:
        yield file
    except Exception as error:
        print(f'Во время записи в файл было возбуждено исключение {error.__class__.__name__}')
        file.truncate(cursor)
#       file.seek(cursor)
#       file.truncate()
    finally:
        file.close()


from io import StringIO
from contextlib import contextmanager
@contextmanager
def safe_write(filename):
    buffer = StringIO()
    try:
        yield buffer
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(buffer.getvalue())
    except Exception as e:
        print(f'Во время записи в файл было возбуждено исключение {type(e).__name__}')
    finally:
        buffer.close()
# ----------------------------------------
from contextlib import contextmanager
@contextmanager
def safe_open(filename, mode='r'):
    file = None
    try:
        try:
            file = open(filename, mode=mode)
            yield (file, None)
        except Exception as error:
            yield (file, error)
    finally:
        if file:
            file.close()


from contextlib import contextmanager
@contextmanager
def safe_open(filename, mode='r'):   
    try:
        with open(filename, mode) as file:    
            yield file, None
    except Exception as error: 
        yield None, error
# ======================================== 6.8
import keyword
class NonKeyword:
    def __init__(self, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        elif self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if isinstance(value, str) and keyword.iskeyword(value):
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value
# ----------------------------------------
class NonNegativeInteger:
    def __init__(self, attr, default=None):
        self._attr = attr
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        elif self._attr not in obj.__dict__:
            if self._default is None:
                raise AttributeError('Атрибут не найден')
            return self._default
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value


class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._attr = name
        self._default = default

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__ and self._default is None:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__.get(self._attr, self._default)

    def __set__(self, obj, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value
# ----------------------------------------
class MaxCallsException(Exception):
    pass

class LimitedTakes:
    def __set_name__(self, owner, attr):
        self._attr = attr

    def __init__(self, times):
        self._times = times

    def __get__(self, obj, cls):
        if obj is None:
            return self
        elif self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        elif self._times <= 0:
            raise MaxCallsException('Превышено количество доступных обращений')
        else:
            self._times -= 1
            return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value
# ----------------------------------------
class TypeChecked:
    def __set_name__(self, owner, attr):
        self._attr = attr

    def __init__(self, *args, **kwargs):
        self._all_args = (*args, *kwargs.values())

    def __get__(self, obj, cls):
        if obj is None:
            return self
        elif self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if not isinstance(value, self._all_args):
            raise TypeError('Некорректное значение')
        obj.__dict__[self._attr] = value
# ----------------------------------------
from random import randint
class RandomNumber:
    def __set_name__(self, owner, attr):
        self._attr = attr

    def __init__(self, start, end, cache=False):
        self._start = start
        self._end = end
        self._cache = cache
        self._rand = randint(self._start, self._end)

    def __get__(self, obj, cls):
        if obj is None:
            return self
        elif self._cache:
            return self._rand
        return randint(self._start, self._end)

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')
# ----------------------------------------
class Versioned:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        elif self._name not in instance.__dict__:
            raise AttributeError('Атрибут не найден')
        return instance.__dict__[self._name][-1]

    def __set__(self, instance, value):
        instance.__dict__.setdefault(self._name, []).append(value)
#       instance.__dict__[self._name] = (*instance.__dict__.get(self._name, ()), value)

    def get_version(self, instance, n):
        return instance.__dict__[self._name][n - 1]

    def set_version(self, instance, n):
        self.__set__(instance, self.get_version(instance, n))
# ======================================== 7.1
class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class WaterVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass

class Motorcycle(LandVehicle):
    pass

class Bicycle(LandVehicle):
    pass

class Propeller(AirVehicle):
    pass

class Jet(AirVehicle):
    pass
# ----------------------------------------
class Shape:
    pass

class Polygon(Shape):
    pass

class Circle(Shape):
    pass

class Quadrilateral(Polygon):
    pass

class Triangle(Polygon):
    pass

class IsoscelesTriangle(Triangle):
    pass

class EquilateralTriangle(Triangle):
    pass

class Parallelogram(Quadrilateral):
    pass

class Rectangle(Parallelogram):
    pass

class Square(Rectangle):
    pass
# ----------------------------------------
class Animal:
    def sleep(self):
        pass

    def eat(self):
        pass

class Fish(Animal):
    def swim(self):
        pass

class Bird(Animal):
    def lay_eggs(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        pass
# ----------------------------------------
class User:
    def __init__(self, name):
        self.name = name

    def skip_ads(self):
        return False

class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)

    def skip_ads(self):
        return True
# ----------------------------------------
class Validator:
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return None

class NumberValidator(Validator):
    def __init__(self, obj):
        super().__init__(obj)

    def is_valid(self):
        return True if isinstance(self.obj, int | float) else False
# ----------------------------------------
class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)

class NonDecCounter(Counter):
    def dec(self, n=1):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        self.limit = limit

    def inc(self, n=1):
        self.value = min(self.value + n, self.limit)
# ======================================== 7.2
class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'

class SilverPlan(BasicPlan):
    has_HD = True
    num_of_devices = 2
    price = '12.99$'

class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'
# ----------------------------------------
class WeatherWarning:
    def rain(self):
        print('Ожидаются сильные дожди и ливни с грозой')

    def snow(self):
        print('Ожидается снег и усиление ветра')

    def low_temperature(self):
        print('Ожидается сильное понижение температуры')

class WeatherWarningWithDate(WeatherWarning):
    def rain(self, date):
        print(f'{date:%d.%m.%Y}')
        super().rain()

    def snow(self, date):
        print(f'{date:%d.%m.%Y}')
        super().snow()

    def low_temperature(self, date):
        print(f'{date:%d.%m.%Y}')
        super().low_temperature()
# ----------------------------------------
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
# ----------------------------------------
class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)

class DoubledCounter(Counter):
    def inc(self, n=1):
        super().inc(n * 2)

    def dec(self, n=1):
        super().dec(n * 2)
# ----------------------------------------
from itertools import zip_longest, starmap
class Summator:
    def total(self, n, m=1):
        return sum(starmap(pow, zip_longest(range(1, n + 1), (), fillvalue=m)))

class SquareSummator(Summator):
    def total(self, n, m=2):
        return super().total(n, m)

class QubeSummator(Summator):
    def total(self, n, m=3):
        return super().total(n, m)

class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m

    def total(self, n):
        return super().total(n, self.m)


class Summator:
    def __init__(self, m=1):
        self.m = m
        
    def total(self, n):
        return sum(map(lambda x: x**self.m, range(1, n+1)))

class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)

class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)
        
class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(m)
# ----------------------------------------
class FieldTracker:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if self.__dict__.get('tracker', None) is None:
            self.__dict__['tracker'] = {}
        if self.tracker.get(key, None) is None:
            self.tracker.setdefault(key, []).append(value)
        elif self.tracker[key][-1] != value:
            self.tracker.setdefault(key, []).append(value)

    def base(self, name):
        return self.tracker[name][0]

    def has_changed(self, name):
        return True if len(self.tracker[name]) > 1 else False

    def changed(self):
        return {k: v[0] for k, v in self.tracker.items() if len(v) > 1}

    def save(self):
        self.__dict__['tracker'] = {k: [v[-1]] for k, v in self.tracker.items()}


class FieldTracker:
    fields = tuple()

    def __init__(self):
        self.dic = {k: self.__dict__[k] for k in self.fields}
        
    def base(self, name):
        return self.dic[name]
    
    def has_changed(self, name):
        return self.dic[name] != self.__dict__[name]
    
    def changed(self):
        return {k: self.dic[k] for k in self.fields if self.has_changed(k)}
    
    def save(self):
        self.dic = {k: self.__dict__[k] for k in self.fields}
# ======================================== 7.3
class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()
# ----------------------------------------
class LowerString(str):
    def __new__(cls, value=''):
        instance = super().__new__(cls, str(value).lower())
        return instance
# ----------------------------------------
class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, str):
            return self.lower() == other.lower()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, str):
            return self.lower() != other.lower()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, str):
            return self.lower() < other.lower()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, str):
            return self.lower() > other.lower()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, str):
            return self.lower() >= other.lower()
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, str):
            return item.lower() in self.lower()
        return NotImplemented


from functools import total_ordering
@total_ordering
class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, str):
            return self.lower() == other.lower()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __contains__(self, substring):
        if isinstance(substring, str):
            return substring.lower() in self.lower()
        return NotImplemented
    
    __lt__ = getattr(object, '__lt__', None)
    __gt__ = getattr(object, '__gt__', None)
    __ge__ = getattr(object, '__ge__', None)
    __ne__ = getattr(object, '__ne__', None)
#   __lt__ = object.__lt__
#   __gt__ = object.__gt__
#   __ge__ = object.__ge__
#   __ne__ = object.__ne__
# ----------------------------------------
class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance

    def title(self):
        return self.text_title
# ----------------------------------------
class SuperInt(int):
    def repeat(self, n=2):
        return SuperInt(super().__str__() + str(abs(self)) * (n - 1))

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        yield from (SuperInt(i) for i in str(self) if i.isdigit())


class SuperInt(int):
    def repeat(self, n=2):
        digit = f"{'-' * (self < 0)}{f'{abs(self)}' * n}"
        return type(self)(digit)

    def to_bin(self):
        return f'{self:b}'

    def next(self):
        return type(self)(self + 1)

    def prev(self):
        return type(self)(self - 1)

    def __iter__(self):
        yield from map(SuperInt, str(abs(self)))
# ----------------------------------------
class RoundedInt(int):
    def __new__(cls, num, even=True):
        return super().__new__(cls, (num + even) // 2 * 2 + (not even))
#       return super().__new__(cls, num + (num % 2 == even))
# ----------------------------------------
from itertools import chain
class AdvancedTuple(tuple):
    def __add__(self, other):
        if '__iter__' in dir(other):
            return __class__(chain(self, other))
        return NotImplemented

    def __radd__(self, other):
        if '__iter__' in dir(other):
            return __class__(chain(other, self))
        return NotImplemented

    __iadd__ = __add__


class AdvancedTuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented

    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(other) + tuple(self))
        return NotImplemented

    def __iadd__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented
# ----------------------------------------
class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        instance = super().__new__(cls, (i % size for i in iterable))
        return instance


class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100, *args, **kwargs):
        iterable = map(lambda item: item % size, iterable)
        instance = super().__new__(cls, iterable)
        return instance
# ======================================== 7.4
from collections import UserList
class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(iterable)
        self.default = default

    def __getitem__(self, item):
        try:
            return self.data[item]
        except IndexError:
            return self.default


from collections import UserList
class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self._default = default

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return self._default
# ----------------------------------------
class EasyDict(dict):
    def __getattr__(self, item):
        return super().__getitem__(item)


class EasyDict(dict):
    __getattr__ = dict.__getitem__


class EasyDict(dict):
    def __getattr__(self, item):
        return self[item]
# ----------------------------------------
from collections import UserDict
class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data.__setitem__(key, value)
        self.data.__setitem__(value, key)
# ----------------------------------------
class AdvancedList(list):
    def join(self, sep=' '):
        return sep.join(map(str, self))

    def map(self, func):
        for index in range(len(self)):
            super().__setitem__(index, func(self[index]))
            # self[i] = func(self[i])

    def filter(self, func):
        temp = list(filter(func, self))
        self.clear()
        self.extend(temp)


class AdvancedList(list):
    def join(self, sep=" "):
        return sep.join(str(item) for item in self)

    def map(self, func):
        self[:] = map(func, self)

    def filter(self, func):
        self[:] = filter(func, self)


class AdvancedList(list):
    def join(self, delimiter=" "):
        return delimiter.join(map(str, self))

    def map(self, func):
        self.__init__(list(map(func, self)))

    def filter(self, func):
        self.__init__(list(filter(func, self)))
# ----------------------------------------
from collections import UserList
class NumberList(UserList):
    @staticmethod
    def check(item):
        if not isinstance(item, int | float):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return item

    def __init__(self, iterable):
        super().__init__(self.check(item) for item in iterable)

    def __setitem__(self, index, item):
        self.data[index] = self.check(item)

    def __add__(self, other):
        if isinstance(other, NumberList):
            return self.__class__(self.data + other.data)
        elif isinstance(other, type(self.data)):
            return self.__class__(self.data + list(self.check(item) for item in other))
        return self.__class__(self.data + list(self.check(item) for item in list(other)))

    def __radd__(self, other):
        if isinstance(other, NumberList):
            return self.__class__(other.data + self.data)
        elif isinstance(other, type(self.data)):
            return self.__class__(list(self.check(item) for item in other) + self.data)
        return self.__class__(list(self.check(item) for item in list(other)) + self.data)

    def __iadd__(self, other):
        if isinstance(other, NumberList):
            self.data += other.data
        elif isinstance(other, type(self.data)):
            self.data += list(self.check(item) for item in other)
        else:
            self.data += list(self.check(item) for item in list(other))
        return self

    def insert(self, index, item):
        self.data.insert(index, self.check(item))

    def append(self, item):
        self.data.append(self.check(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            self.data.extend(other)
        else:
            self.data.extend(self.check(item) for item in other)


from collections import UserList
class NumberList(UserList):
    @staticmethod
    def check(item):
        if not isinstance(item, int | float):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        return item

    def __init__(self, iterable):
        super().__init__(self.check(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, self.check(item))

    def __add__(self, other):
        return super().__add__(self.check(item) for item in other)

    def __radd__(self, other):
        return super().__radd__(self.check(item) for item in other)

    def __iadd__(self, other):
        return super().__iadd__(self.check(item) for item in other)

    def insert(self, index, item):
        super().insert(index, self.check(item))

    def append(self, item):
        super().append(self.check(item))

    def extend(self, other):
        super().extend(self.check(item) for item in other)
# ----------------------------------------
class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k

    def keys_of(self, value):
        return (k for k, v in self.items() if v == value)
# ----------------------------------------
from collections import UserDict
class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if value in self.data.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        self.data.__setitem__(key, value)
# ----------------------------------------
from collections import UserString
class MutableString(UserString):
    def __setitem__(self, key, value):
        data_list = list(self.data)
        data_list[key] = value
        self.data = ''.join(data_list)

    def __delitem__(self, key):
        data_list = list(self.data)
        del data_list[key]
        self.data = ''.join(data_list)

    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(list(self.data), key=key, reverse=reverse))
# ======================================== 7.5
from abc import ABC, abstractmethod
class Middle(ABC):
    def __init__(self, user_votes, expert_votes):
        self.user_votes = user_votes                   # пользовательские оценки
        self.expert_votes = expert_votes               # оценки критиков

    def get_correct_user_votes(self):
        """Возвращает нормализованный список пользовательских оценок
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.user_votes if 10 < vote < 90]

    def get_correct_expert_votes(self):
        """Возвращает нормализованный список оценок критиков
        без слишком низких и слишком высоких значений"""
        return [vote for vote in self.expert_votes if 5 < vote < 95]
    
    @abstractmethod
    def get_average(self):
        pass

class Average(Middle):
    def get_average(self, users=True):
        """Возвращает среднее арифметическое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return sum(votes) / len(votes)

class Median(Middle):
    def get_average(self, users=True):
        """Возвращает медиану пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = sorted(self.get_correct_user_votes())
        else:
            votes = sorted(self.get_correct_expert_votes())

        return votes[len(votes) // 2]

class Harmonic(Middle):
    def get_average(self, users=True):
        """Возвращает среднее гармоническое пользовательских оценок или
        оценок критиков в зависимости от значения параметра users"""
        if users:
            votes = self.get_correct_user_votes()
        else:
            votes = self.get_correct_expert_votes()

        return len(votes) / sum(map(lambda vote: 1 / vote, votes))
# ----------------------------------------
from abc import ABC, abstractmethod
class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, *args, **kwargs):
        pass

class King(ChessPiece):
    def can_move(self, h, v):
        return ((ord(self.horizontal) - ord(h)) ** 2 + (self.vertical - v) ** 2 in (1, 2))

class Knight(ChessPiece):
    def can_move(self, h, v):
        return ((ord(self.horizontal) - ord(h)) ** 2 + (self.vertical - v) ** 2 == 5)


from abc import ABC, abstractmethod
class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        return ((ord(self.horizontal) - ord(horizontal)) ** 2 + (self.vertical - vertical) ** 2)

class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        return super().can_move(horizontal, vertical) in (1, 2)

class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        return super().can_move(horizontal, vertical) == 5
# ----------------------------------------
from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        elif self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self.validate(value=value):
            obj.__dict__[self._attr] = value

    def __delete__(self, obj):
        if self._attr in obj.__dict__:
            del obj.__dict__[self._attr]

    @abstractmethod
    def validate(self, value):
        pass

class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        elif self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        elif self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True

class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        elif self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        elif self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        elif self.predicate and not self.predicate(value):
            raise ValueError(f'Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True
# ----------------------------------------
from collections.abc import Iterable, Iterator

def is_iterable(obj):
    return isinstance(obj, Iterable)

def is_iterator(obj):
    return isinstance(obj, Iterator)
# ----------------------------------------
from collections.abc import Sequence

class CustomRange(Sequence):
    def __init__(self, *args):
        self._data = []
        for el in args:
            if isinstance(el, int):
                self._data.append(el)
            elif isinstance(el, str):
                start, stop = map(int, el.split('-'))
                self._data.extend(range(start, stop + 1))

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __len__(self):
        return len(self._data)
# ----------------------------------------
from collections.abc import Sequence

class BitArray(Sequence):
    def __init__(self, iterable=()):
        self._data = list(iterable)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def __reversed__(self):
        return list(reversed(self._data))

    def __invert__(self):
        return __class__(int(not i) for i in self._data)

    def __and__(self, other):
        if isinstance(other, __class__) and len(self) == len(other):
            return __class__(el1 & el2 for el1, el2 in zip(self._data, other._data))
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, __class__) and len(self._data) == len(other._data):
            return __class__(el1 | el2 for el1, el2 in zip(self._data, other._data))
        return NotImplemented
# ----------------------------------------
from collections.abc import Sequence

class DNA(Sequence):
    __MAP = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}

    def __init__(self, chain=''):
        self._data = chain

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item], __class__.__MAP[self._data[item]]
        return NotImplemented

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return self._data

    def __contains__(self, item):
        return item in self._data

    def __eq__(self, other):
        if isinstance(other, __class__):
            return self._data == other._data
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self._data + other._data)
        return NotImplemented

#   __class__ == type(self)
#   True
# ----------------------------------------
from collections.abc import Sequence

class SortedList(Sequence):
    def __init__(self, iterable=()):
        self._data = sorted(iterable)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        return NotImplemented

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __delitem__(self, key):
        del self._data[key]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'{__class__.__name__}({self._data})'

    def __contains__(self, item):
        return item in self._data

    def __add__(self, other):
        if isinstance(other, __class__):
            return __class__(self._data + other._data)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, __class__):
            self._data.extend(other._data)
            self._data.sort()
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return __class__(item for item in self._data for _ in range(other))
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self._data = list(item for item in self._data for _ in range(other))
            return self
        return NotImplemented

    def add(self, obj):
        self._data.append(obj)
        self._data.sort()

    def discard(self, obj):
        while obj in self._data:
            self._data.remove(obj)

    def update(self, iterable):
        self._data.extend(iterable)
        self._data.sort()

    @staticmethod
    def _raise_error(*args, **kwargs):
        raise NotImplementedError

    append = insert = extend = reverse = __reversed__ = _raise_error
# ======================================== 7.6
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

class E(B, D):
    pass
# ----------------------------------------
class H:
    pass

class D(H):
    pass

class E(H):
    pass

class F(H):
    pass

class G(H):
    pass

class B(D, E):
    pass

class C(F, G):
    pass

class A(B, C):
    pass
# ----------------------------------------
def get_method_owner(cls, method):
    for class_ in cls.mro():
#   for class_ in cls.__mro__:
        if method in class_.__dict__:
            return class_
# ----------------------------------------
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, mood='neutral'):
        self.mood = mood

    @abstractmethod
    def greet(self):
        pass

class Father(Person):
    def greet(self):
        return 'Hello!'

    def be_strict(self):
        self.mood = 'strict'

class Mother(Person):
    def greet(self):
        return 'Hi, honey!'

    def be_kind(self):
        self.mood = 'kind'

class Daughter(Mother, Father):
    pass

class Son(Father, Mother):
    pass
# ----------------------------------------
class MROHelper:
    @staticmethod
    def len(cls):
        return len(cls.mro())

    @staticmethod
    def class_by_index(cls, n=0):
        return cls.mro()[n]

    @staticmethod
    def index_by_class(child, parent):
        return child.mro().index(parent)
# ======================================== 7.7
from datetime import date
from abc import ABC, abstractmethod

class Date(ABC):
    def __init__(self, year, month, day):
        self._date = date(year, month, day)

    def iso_format(self):
        return self._date.isoformat()

    @abstractmethod
    def format(self):
        pass

class USADate(Date):
    def format(self):
        return self._date.strftime('%m-%d-%Y')
#       return f'{self._date:%m-%d-%Y}'

class ItalianDate(Date):
    def format(self):
        return self._date.strftime('%d/%m/%Y')
#       return f'{self._date:%d/%m/%Y}'


from datetime import date

class Date(date):
    def iso_format(self):
        return self.isoformat()

class USADate(Date):
    def format(self):
        return self.strftime('%m-%d-%Y') 
        
class ItalianDate(Date):
    def format(self):
        return self.strftime('%d/%m/%Y') 
# ----------------------------------------
from abc import ABC, abstractmethod

class Stat(ABC):
    def __init__(self, iterable=()):
        self.data = list(iterable)

    def add(self, num):
        self.data.append(num)

    def clear(self):
        self.data.clear()

    @abstractmethod
    def result(self):
        pass

class MinStat(Stat):
    def result(self):
        return min(self.data, default=None)

class MaxStat(Stat):
    def result(self):
        return max(self.data, default=None)

class AverageStat(Stat):
    def result(self):
        return sum(self.data) / len(self.data) if self.data else None


class Stat(list):
    def add(self, n):
        self.append(n)

class MinStat(Stat):
    def result(self):
        return min(self, default=None)

class MaxStat(Stat):
    def result(self):
        return max(self, default=None)

class AverageStat(Stat):
    def result(self):
        return sum(self) / len(self) if self else None
# ----------------------------------------
from abc import ABC, abstractmethod

class Paragraph(ABC):
    def __init__(self, length):
        self.length = length
        self.data = []

    def add(self, string):
        self.data.extend(string.split())

    @abstractmethod
    def end(self, align=None):
        string_ = ''
        for word in self.data:
            string_ = f'{string_} {word}'
            if len(string_.strip()) > self.length:
                string_to_print, string_ = string_.rsplit(maxsplit=1)
                align_len = self.length if align == '>' else min(len(string_to_print.strip()), self.length)
                print(f'{string_to_print.strip():{align}{align_len}}')
        if string_:
            align_len = self.length if align == '>' else min(len(string_.strip()), self.length)
            print(f'{string_.strip():{align}{align_len}}')
        self.data.clear()

class LeftParagraph(Paragraph):
    def end(self, align='<'):
        super().end(align)

class RightParagraph(Paragraph):
    def end(self, align='>'):
        super().end(align)


import textwrap
from abc import ABC, abstractmethod

class Paragraph(ABC):
    def __init__(self, length):
        self.length = length
        self.data = []

    def add(self, string):
        self.data.extend(string.split())

    @abstractmethod
    def end(self):
        pass

class LeftParagraph(Paragraph):
    def end(self):
        for string in textwrap.wrap(' '.join(self.data), width=self.length):
            print(string)
        self.data.clear()

class RightParagraph(Paragraph):
    def end(self):
        for string in textwrap.wrap(' '.join(self.data), width=self.length):
            print(f'{string:>{self.length}}')
        self.data.clear()
# ======================================== 7.8
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

class Circle:
    def __init__(self, radius, center: Point):
        self.radius = radius
        self.center = center

    def __str__(self):
        return f'{str(self.center)}, r = {self.radius}'
# ----------------------------------------
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'

class ShoppingCart:
    def __init__(self, items=()):
        self.items = list(items)

    def __str__(self):
        return '\n'.join(f'{str(item)}' for item in self.items)

    def add(self, item: Item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def remove(self, name):
        new_items = [item for item in self.items if item.name != name]
        self.items[:] = new_items
# ----------------------------------------
from itertools import product
from random import shuffle

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'

class Deck:
    __SUIT = ['♣', '♢', '♡', '♠']
    __RANK = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck = list(Card(*card) for card in product(__class__.__SUIT, __class__.__RANK))
#       self.deck = [Card(s, r) for s in self.__SUIT for r in self.__RANK]

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'

    def shuffle(self):
        if len(self.deck) == 52:
            shuffle(self.deck)
        else:
            raise ValueError('Перемешивать можно только полную колоду')

    def deal(self):
        if len(self.deck) > 0:
            return self.deck.pop()
        else:
            raise ValueError('Все карты разыграны')
# ----------------------------------------
class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'({self.key!r}, {self.value!r})'

class Queue:
    def __init__(self, pairs=()):
        self.pairs = []
        if isinstance(pairs, dict):
            for k, v in pairs.items():
                self.add((k, v))
        elif isinstance(pairs, list):
            for pair in pairs:
                self.add((pair[0], pair[1]))

    def __repr__(self):
        return f'{__class__.__name__}({self.pairs})'

    def __len__(self):
        return len(self.pairs)

    def add(self, elem):
        elem = Element(*elem)
        pair_to_remove = [pair for pair in self.pairs if pair.key == elem.key]
        if pair_to_remove:
            self.pairs.remove(pair_to_remove[0])
        self.pairs.append(elem)

    def pop(self):
        if not self.pairs:
            raise KeyError('Очередь пуста')
        return self.pairs.pop(0)


from collections import OrderedDict

class Queue:
    def __init__(self, initial_data=None):
        self.data = OrderedDict()
        if initial_data is not None:
            self.data.update(initial_data)

    def add(self, item):
        key, value = item
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value

    def pop(self):
        try:
            return self.data.popitem(last=False)
        except KeyError as e:
            e.args = ('Очередь пуста',)
            raise

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f'Queue({list(self.data.items())})'


from collections import deque

class Queue(deque):
    def add(self, item):
        for elem in self:
            if elem[0]==item[0]:
                del self[self.index(elem)]
                break
        self.append(item)
                
    
    def pop(self):
        if len(self):
            return self.popleft()
        raise KeyError('Очередь пуста')
# ----------------------------------------
from datetime import datetime, timedelta
from itertools import pairwise

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, '%H:%M')
        dt_duration = datetime.strptime(duration, '%H:%M')
        self.duration = timedelta(hours=dt_duration.hour, minutes=dt_duration.minute)
        self.end_time = self.start_time + self.duration

class Conference:
    def __init__(self):
        self.data = []

    def add(self, lecture):
        for lect in self.data:
            if ((lect.start_time <= lecture.start_time < lect.end_time)
                    or (lect.start_time < lecture.end_time <= lect.end_time)
                    or (lecture.start_time < lect.start_time and lect.end_time < lecture.end_time)):
                raise ValueError('Провести выступление в это время невозможно')
        self.data.append(lecture)

    def total(self):
        seconds = sum(lect.duration.seconds for lect in self.data)
        return f'{seconds // 3600:02}:{(seconds % 3600) // 60:02}'

    def longest_lecture(self):
        seconds = max(self.data, key=lambda x: x.duration).duration.seconds
        return f'{seconds // 3600:02}:{(seconds % 3600) // 60:02}'

    def longest_break(self):
        self.data.sort(key=lambda x: x.start_time)
        longest_break = timedelta(0)
        for pair in pairwise(self.data):
            longest_break = max(longest_break, pair[1].start_time - pair[0].end_time)
        seconds = longest_break.seconds
        return f'{seconds // 3600:02}:{(seconds % 3600) // 60:02}'
# ======================================== 8.1
from functools import total_ordering

@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if isinstance(other, __class__):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, __class__):
            return self.area < other.area
        return NotImplemented
# ======================================== 8.2
from enum import Enum

class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        __CODES = {'CONTINUE': 'информация',
                   'OK': 'успех',
                   'USE_PROXY': 'перенаправление',
                   'NOT_FOUND': 'ошибка клиента',
                   'BAD_GATEWAY': 'ошибка сервера'}
        return __CODES[self.name]


#   def code_class(self):
#       groups = ('информация', 'успех', 'перенаправление', 'ошибка клиента', 'ошибка сервера')
#       codes = dict(zip(HTTPStatusCodes, groups))
#       return codes[self]
# ----------------------------------------
from enum import Enum, auto

class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, code):
        __CODES = {
            'WINTER': {'en': 'winter', 'ru': 'зима'},
            'SPRING': {'en': 'spring', 'ru': 'весна'},
            'SUMMER': {'en': 'summer', 'ru': 'лето'},
            'FALL': {'en': 'fall', 'ru': 'осень'}
        }
        return __CODES[self.name][code]
# ----------------------------------------
from enum import IntEnum
from datetime import date, timedelta

Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)

class NextDate:
    def __init__(self, today: date, weekday: Weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        return self.today + timedelta(days=self.days_until())

    def days_until(self):
        if self.weekday == self.today.weekday() and not self.after_today:
            return 7
        return (self.weekday + 7 - self.today.weekday()) % 7
# ======================================== 8.3
from enum import Flag, auto

class OrderStatus(Flag):
    ORDER_PLACED = auto()
    PAYMENT_RECEIVED = auto()
    SHIPPING_COMPLETE = auto()
# ----------------------------------------
from enum import Flag, auto

# MovieGenres = Flag('MovieGenres', ['ACTION', 'COMEDY', 'DRAMA', 'FANTASY', 'HORROR'])
class MovieGenres(Flag):
    ACTION = auto()
    COMEDY = auto()
    DRAMA = auto()
    FANTASY = auto()
    HORROR = auto()

class Movie:
    def __init__(self, name, genres: MovieGenres):
        self.name = name
        self.genres = genres

    def __str__(self):
        return self.name

    def in_genre(self, genre):
        return genre in self.genres
# ======================================== 8.4
import functools

def reverse_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = reversed(args)
        return func(*args, **kwargs)
    return wrapper


import functools

class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = reversed(args)
        return self.func(*args, **kwargs)
# ----------------------------------------
import functools

class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self._times = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self._times <= 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            self._times -= 1
            return func(*args, **kwargs)
        return wrapper
# ----------------------------------------
import functools

class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        all_args = [*args, *kwargs.values()]
        if not all(map(lambda x: isinstance(x, (int, float)), all_args)):
            raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)
# ----------------------------------------
import functools

class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, self.datatype):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper
# ----------------------------------------
import functools

class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
            return (value, None)
        except Exception as e:
            return (None, type(e))
# ----------------------------------------
import functools

class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if type(e) in self.exceptions:
                    print(f'Исключение {e.__class__.__name__} обработано')
                else:
                    raise
        return wrapper


        ...
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.exceptions as e:
                print(f'Исключение {e.__class__.__name__} обработано')
        return wrapper
# ----------------------------------------
import functools

class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for item in zip(map(type, args), self.types):
                if item[0] is not item[1]:
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper


        ...
        def wrapper(*args, **kwargs):
            if all(map(isinstance, args, self.types)):
                return func(*args, **kwargs)
            raise TypeError
        return wrapper
# ======================================== 8.5
import functools

def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls
# ----------------------------------------
def add_attr_to_class(**attrs):
    def decorator(cls):
        for key, value in attrs.items():
            setattr(cls, key, value)
        return cls
    return decorator


class add_attr_to_class:
    def __init__(self, **kwargs):
        self.attrs = kwargs

    def __call__(self, cls):
        for attr_name, attr_value in self.attrs.items():
            setattr(cls, attr_name, attr_value)
        return cls
# ----------------------------------------
import json

def jsonattr(filename):
    def decorator(cls):
        with open(filename, encoding='utf8') as file:
            attrs = json.load(file)
        for key, value in attrs.items():
            setattr(cls, key, value)
        return cls
    return decorator
# ----------------------------------------
import functools

def singleton(cls):
    cls._instance = None
    cls_new = cls.__new__

    @functools.wraps(cls_new)
    def new_singleton(self, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    cls.__new__ = new_singleton
    return cls


import functools

def singleton(cls):
    _instance = object.__new__(cls)
    old_new = cls.__new__
    
    @functools.wraps(old_new)
    def new_new(cls, *args, **kwargs):
        return _instance
    
    cls.__new__ = new_new
    return cls
# ----------------------------------------
import re
# from typing import Callable

def snake_case(attrs=False):
    def to_snake_case(string):
        prefix = '_' if string.startswith('_') else ''
        new_str = re.sub(r'([A-Z])', r'_\1', string).lower().strip('_')
        return prefix + new_str

    def decorator(cls):
        new__dict__ = {}
        for key, value in cls.__dict__.items():
            if ((key.startswith('__') and key.endswith('__')) or (not attrs and not callable(value))):
#           if ((key.startswith('__') and key.endswith('__')) or (not attrs and not isinstance(value, Callable))):
                continue
            new__dict__[key] = value
        for key, value in new__dict__.items():
            delattr(cls, key)
            setattr(cls, to_snake_case(key), value)
        return cls

    return decorator


import re
    ...
    def to_snake_case(string):
        return '_'.join(re.findall(r'[a-zA-Z][^A-Z]*', string)).lower()


from inflection import underscore, camelize
    ...
    def to_snake_case(string):
        return underscore(string)
# ----------------------------------------
def auto_repr(args, kwargs):
    def decorator(cls):
        def new_repr(self):
            args_, kwargs_ = [], []
            for key, value in self.__dict__.items():
                if key in args:
                    args_.append(f'{value!r}')
                if key in kwargs:
                    kwargs_.append(f'{key}={value!r}')
            return f'{cls.__name__}({", ".join(args_ + kwargs_)})'

        cls.__repr__ = new_repr
        return cls

    return decorator


def auto_repr(args, kwargs):
    def wrapper(cls):
        def __repr__(self):
            cls_args = [repr(self.__dict__[k]) for k in args]
            cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
            return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'

        cls.__repr__ = __repr__
        return cls

    return wrapper
# ----------------------------------------
import functools

def limiter(limit, unique, lookup):
    def decorator(cls):
        LOOKUPS = {"LAST": -1, "FIRST": 0}
        instances = {}
        cls_init = cls.__init__

        @functools.wraps(cls.__new__)
        def __new__(self, *args, **kwargs):
            instance = object.__new__(cls)
            cls_init(instance, *args, **kwargs)
            if len(instances) < limit and getattr(instance, unique) not in instances:
                instances.setdefault(getattr(instance, unique), instance)
            instance = instances.get(getattr(instance, unique), None)
            if instance is None:
                instance = tuple(instances.values())[LOOKUPS[lookup]]
            return instance

        cls.__new__ = __new__
        cls.__init__ = object.__init__  # Блокируем автоматический вызов инициализатора
        return cls

    return decorator


def limiter(limit, unique, lookup):
    instances = {}
    lookups = {}

    def wrapper(cls):
        def get_instance(*args, **kwargs):
            instance = cls(*args, **kwargs)
            lookups.setdefault('FIRST', instance)
            identifier = getattr(instance, unique)
            if len(instances) < limit:
                if identifier not in instances:
                    lookups['LAST'] = instances[identifier] = instance
                return instances[identifier]
            return instances.get(identifier) or lookups.get(lookup)

        return get_instance

    return wrapper
# ======================================== 8.6
class City:
    def __init__(self, name, population, founded):
        self.name = name
        self.population = population
        self.founded = founded

    def __repr__(self):
        return f"City(name='{self.name}', population={self.population}, founded={self.founded})"

    def __eq__(self, other):
        if isinstance(other, City):
            return (self.name, self.population, self.founded) == (other.name, other.population, other.founded)
        return NotImplemented


from dataclasses import dataclass

@dataclass
class City:
    name: str
    population: int
    founded: int


from dataclasses import make_dataclass

City = make_dataclass('City', ('name', 'population', 'founded'))
# ----------------------------------------
from dataclasses import dataclass, field

@dataclass(frozen=True)
class MusicAlbum:
    title: str
    artist: str
    genre: str = field(repr=False, compare=False)
    year: int = field(repr=False)
# ----------------------------------------
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = 0

    def __post_init__(self):
        if 0 < self.x < 90:
            if 0 < self.y < 90:
                self.quadrant = 1
            if -90 < self.y < 0:
                self.quadrant = 4
        if -90 < self.x < 0:
            if 0 < self.y < 90:
                self.quadrant = 2
            if -90 < self.y < 0:
                self.quadrant = 3

    def symmetric_x(self):
        return __class__(self.x, -self.y)

    def symmetric_y(self):
        return __class__(-self.x, self.y)


    ...
    def __post_init__(self):
        self.quadrant = {
            self.x > 0 and self.y > 0: 1,
            self.x > 0 and self.y < 0: 4,
            self.x < 0 and self.y < 0: 3,
            self.x < 0 and self.y > 0: 2}.get(True, 0)
# ----------------------------------------
from dataclasses import dataclass, field

@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)

@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, compare=False, repr=False)

    def add_players(self, *args):
        self.players.extend(args)
# ======================================== 9.1
class Anything:
    def __eq__(self, other):
        return True

    __ne__ = __lt__ = __le__ = __gt__ = __ge__ = __eq__

def anything():
    return Anything()
# ----------------------------------------
class Vector:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f'{self.args}'

    def __add__(self, other):
        self.check_len(other)
        if isinstance(other, __class__):
            return __class__(*(x + y for x, y in zip(self.args, other.args)))
        return NotImplemented

    def __sub__(self, other):
        self.check_len(other)
        if isinstance(other, __class__):
            return __class__(*(x - y for x, y in zip(self.args, other.args)))
        return NotImplemented

    def __mul__(self, other):
        self.check_len(other)
        if isinstance(other, __class__):
            return sum(x * y for x, y in zip(self.args, other.args))
        return NotImplemented

    def __eq__(self, other):
        self.check_len(other)
        if isinstance(other, __class__):
            return self.args == other.args
        return NotImplemented

    def norm(self):
        return sum(arg**2 for arg in self.args)**0.5

    def check_len(self, other):
        if len(self.args) != len(other.args):
            raise ValueError('Векторы должны иметь равную длину')
# ----------------------------------------
from string import ascii_lowercase as ABC

class CaesarCipher:
    _CASE = {True: str.upper, False: str.lower}

    def __init__(self, shift):
        self.shift = shift

    def encode(self, string):
        new_string = []
        for l in string:
            if l.isascii() and l.isalpha():
                case = __class__._CASE[l.isupper()]
                l = case((ABC * 2)[ABC.index(l.lower()) + self.shift])
            new_string.append(l)
        return ''.join(new_string)

    def decode(self, string):
        new_string = []
        for l in string:
            if l.isascii() and l.isalpha():
                case = __class__._CASE[l.isupper()]
                l = case((ABC * 2)[(ABC * 2).index(l.lower(), len(ABC)) - self.shift])
            new_string.append(l)
        return ''.join(new_string)


from string import ascii_lowercase as low, ascii_uppercase as up

class CaesarCipher:
    def __init__(self, shift):
        self._in = low + up
        self._out = low[shift:] + low[:shift] + up[shift:] + up[:shift]

    def encode(self, string):
        return string.translate(string.maketrans(self._in, self._out))

    def decode(self, string):
        return string.translate(string.maketrans(self._out, self._in))
# ----------------------------------------
from abc import ABC, abstractmethod

class Progression(ABC):
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        pass

class ArithmeticProgression(Progression):
    def __next__(self):
        value = self.start
        self.start += self.step
        return value

class GeometricProgression(Progression):
    def __next__(self):
        value = self.start
        self.start *= self.step
        return value


import operator

class Progression(abc.ABC):
    func = None
    def __init__(self, first, shift):
        self._current = first
        self._shift = shift

    def __iter__(self):
        return self

    def __next__(self):
        res = self._current
        self._current = self.func(self._current, self._shift)
        return res

class ArithmeticProgression(Progression):
    func = operator.add

class GeometricProgression(Progression):
    func = operator.mul
# ----------------------------------------
iimport re

class DomainException(Exception):
    pass

class Domain:
    __CORRECT_DOMAIN = fr'[a-zA-Z]+\.[a-zA-Z]+'
    __CORRECT_URL = fr'https?://{__CORRECT_DOMAIN}'
    __CORRECT_EMAIL = fr'[a-zA-Z]+@{__CORRECT_DOMAIN}'

    def __init__(self, string):
        if not bool(re.fullmatch(self.__CORRECT_DOMAIN, string)):
            raise DomainException('Недопустимый домен, url или email')
        self.string = string

    def __repr__(self):
        return f'{self.string}'

    @classmethod
    def from_url(cls, string):
        if not bool(re.fullmatch(cls.__CORRECT_URL, string)):
            raise DomainException('Недопустимый домен, url или email')
        return cls(string.split('//')[-1])

    @classmethod
    def from_email(cls, string):
        if not bool(re.fullmatch(cls.__CORRECT_EMAIL, string)):
            raise DomainException('Недопустимый домен, url или email')
        return cls(string.split('@')[-1])


# extract group (domain) from re
import re

class DomainException(Exception):
    pass

class Domain:
    __CORRECT_DOMAIN = r'\w+\.\w+'
    __CORRECT_URL = fr'^https?://(?P<domain>{__CORRECT_DOMAIN})$'
    __CORRECT_EMAIL = fr'\w+@(?P<domain>{__CORRECT_DOMAIN})'

    def __init__(self, domain):
        if not re.fullmatch(self.__CORRECT_DOMAIN, domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    def __str__(self):
        return self.domain

    @classmethod
    def from_url(cls, url):
        url = re.match(cls.__CORRECT_URL, url)
        if not url:
            raise DomainException('Недопустимый домен, url или email')
        return cls(url.group('domain'))

    @classmethod
    def from_email(cls, email):
        email = re.match(cls.__CORRECT_EMAIL, email)
        if not email:
            raise DomainException('Недопустимый домен, url или email')
        return cls(email.group('domain'))
# ----------------------------------------
class HighScoreTable:
    def __init__(self, limit):
        self.limit = limit
        self.scores = []

    def update(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.scores[self.limit:] = []

    def reset(self):
        self.scores.clear()
# ----------------------------------------
from math import ceil

class Pagination:
    def __init__(self, items, size):
        self.items = items
        self.size = size
        self.page = 1

    def get_visible_items(self):
        return self.items[(self.page - 1) * self.size: self.page * self.size]

    def prev_page(self):
        self.page = max(1, self.page - 1)
        return self

    def next_page(self):
        self.page = min(ceil(len(self.items) / self.size), self.page + 1)
        return self

    def first_page(self):
        self.page = 1
        return self

    def last_page(self):
        self.page = ceil(len(self.items) / self.size)
        return self

    def go_to_page(self, page):
        if page < 1:
            self.page = 1
        elif page > self.last_page().page:
            self.page = self.last_page().page
        else:
            self.page = page
        return self

    @property
    def total_pages(self):
        return ceil(len(self.items) / self.size)

    @property
    def current_page(self):
        return self.page
# ----------------------------------------
from dataclasses import dataclass, field

@dataclass
class Testpaper:
    subject: str
    test: list
    threshold: str

class Student:
    def __init__(self):
        self._tests_taken = {}

    def take_test(self, testpaper, student_test):
        result = round(sum(x == y for x, y in zip(testpaper.test, student_test)) / len(student_test) * 100)
        self._tests_taken[testpaper.subject] = ('Passed!' if result >= int(testpaper.threshold.strip('%')) else 'Failed!') + f' ({result}%)'

    @property
    def tests_taken(self):
        return self._tests_taken if self._tests_taken else 'No tests taken'
# ----------------------------------------
class TicTacToe:
    __MARK = {False: 'O', True: 'X'}

    def __init__(self):
        self.field = [[' '] * 3 for _ in range(3)]
        self.first = True

    def mark(self, col, row):
        if self.is_winner() or self.is_draw():
            print('Игра окончена')
            return None
        elif self.field[col - 1][row - 1] == ' ':
            self.field[col - 1][row - 1] = self.__MARK[self.first]
            self.first = not self.first
        else:
            print('Недоступная клетка')

    def is_winner(self):
        for x in range(3):
            if ((self.field[x][0] + self.field[x][1] + self.field[x][2] in ['XXX', 'OOO']) or
                    (self.field[0][x] + self.field[1][x] + self.field[2][x] in ['XXX', 'OOO']) or
                    (self.field[0][0] + self.field[1][1] + self.field[2][2] in ['XXX', 'OOO']) or
                    (self.field[0][2] + self.field[1][1] + self.field[2][0] in ['XXX', 'OOO'])):
                return self.__MARK[not self.first]

    def winner(self):
        winner = self.is_winner()
        if winner:
            return winner
        elif self.is_draw():
            return 'Ничья'

    def is_draw(self):
        if len(''.join([item for row in self.field for item in row]).replace(' ', '')) == 9:
            return True

    def show(self):
        print(*self.field[0], sep='|')
        print('-----')
        print(*self.field[1], sep='|')
        print('-----')
        print(*self.field[2], sep='|')
# ----------------------------------------
from dataclasses import dataclass, field
from random import sample

@dataclass
class Cell:
    row: int
    col: int
    mine: bool
    neighbours: int = field(init=False)

@dataclass
class Game:
    rows: int
    cols: int
    mines: bool
    board: list = field(init=False)

    def __post_init__(self):
        board_mines = sample([True, False],
                             counts=[self.mines, self.rows * self.cols - self.mines],
                             k=self.rows * self.cols)
        self.board = [[Cell(r, c, board_mines.pop()) for c in range(self.cols)] for r in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                self.board[r][c].neighbours = get_neighbours_count(r, c, self)
# ----------------------------------------
import operator

class Currency:
    __RATE = {'EUR': {'RUB': 90, 'USD': 1.1, 'EUR': 1},
            'USD': {'RUB': 90 / 1.1, 'EUR': 1 / 1.1, 'USD': 1},
            'RUB': {'EUR': 1 / 90, 'USD': 1.1 / 90, 'RUB': 1}}

    def __init__(self, amount, curr):
        self.amount = amount
        self.curr = curr

    def __str__(self):
        return f'{round(self.amount, 2)} {self.curr}'

    def __add__(self, other):
        return self.operation(other, func=operator.add)

    def __sub__(self, other):
        return self.operation(other, func=operator.sub)

    def __mul__(self, other):
        return self.operation(other, func=operator.mul)

    def __truediv__(self, other):
        return self.operation(other, func=operator.truediv)

    def operation(self, other, func):
        if isinstance(other, __class__):
            return __class__(func(self.amount, (other.amount * self.__RATE[other.curr][self.curr])), self.curr)
        return NotImplemented

    def change_to(self, new_curr):
        self.amount = self.amount * self.__RATE[self.curr][new_curr]
        self.curr = new_curr
# ----------------------------------------
class Selfie:
    def __init__(self):
        self.states = []

    def save_state(self):
        new_state = {k: v for k, v in self.__dict__.items() if k != 'states'}
        self.states.append(new_state)

    def recover_state(self, n):
        try:
            new = Selfie()
            new.__dict__.update(self.states[n])
            new.__dict__['states'] = self.states[:n]
            return new
        except IndexError:
            del new
            return self

    def n_states(self):
        return len(self.__dict__['states'])

# !!! memory leakage
import pickle
from itertools import count

class Selfie:
    def __init__(self):
        self._states = {}
        self._state = count()

    def save_state(self):
        self._states[next(self._state)] = pickle.dumps(self)

    def recover_state(self, n):
        obj = self._states.get(n)
        return pickle.loads(obj) if obj else self

    def n_states(self):
        return len(self._states)


# !!! memory leakage
from copy import deepcopy

class Selfie:
    def __init__(self):
        self.states = {}

    def save_state(self):
        self.states[len(self.states)] = deepcopy(self)

    def recover_state(self, n):
        return self.states[n] if n in self.states else self

    def n_states(self):
        return len(self.states)
# ----------------------------------------
from collections import UserDict

class MultiKeyDict(UserDict):
    def __setitem__(self, key, value):
        key = self.get_key(key)
        self.data.__setitem__(key, value)

    def __getitem__(self, item):
        key = self.get_key(item)
        return self.data[key]

    def __delitem__(self, item):
        key = self.get_key(item)
        # del key
        for key_tuple in self.data:
            if len(key_tuple) == 1:
                del self.data[key_tuple]
                break
            elif key[0] == key_tuple[0]:
                temp = self.data[key_tuple]
                del self.data[key_tuple]
                new_key = tuple([None] + list(key_tuple)[1:])
                self.data[new_key] = temp
                break

    def get_key(self, key):
        key_main, key_alias = None, None
        for key_tuple in self.data:
            if key in key_tuple:
                if key == key_tuple[0]:
                    key_main = key_tuple
                else:
                    key_alias = key_tuple
        return key_main or key_alias or (key,)

    def alias(self, key, alias):
        # del alias
        for key_tuple in self.data:
            if alias in key_tuple[1:]:
                temp = self.data[key_tuple]
                del self.data[key_tuple]
                list_ = list(key_tuple[1:])
                list_.remove(alias)
                new_key = tuple([key_tuple[0]] + list_)
                self.data[new_key] = temp
                break
        # add alias
        for key_tuple in self.data:
            if key == key_tuple[0]:
                temp = self.data[key_tuple]
                del self.data[key_tuple]
                new_key = tuple(list(key_tuple) + [alias])
                self.data[new_key] = temp
                break


from collections import UserDict

class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, alias):
        self._aliases[alias] = key

    def __getitem__(self, key):
        get_item = self.data.get
        item = get_item(key)

        if item is not None:
            return item
        return get_item(self._aliases[key])

    def __setitem__(self, key, value):
        if key in self.data or key not in self._aliases:
            self.data[key] = value
        else:
            self.data[self._aliases[key]] = value

    def __delitem__(self, del_key):
        flag = False
        new_key = None
        alias_keys = []

        if del_key in self._aliases.values():
            for alias_key, key in self._aliases.items():
                if key == del_key and flag is False:
                    self.data[alias_key] = self.data[del_key]
                    new_key = alias_key
                    flag = True
                elif key == del_key and flag is True:
                    alias_keys.append(alias_key)

        if new_key is not None:
            self._aliases.update(dict.fromkeys(alias_keys, new_key))

        del self.data[del_key]
# ----------------------------------------
class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        def and_func(*args, **kwargs):
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)

        return and_func

    def __or__(self, other):
        def or_func(*args, **kwargs):
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)

        return or_func

    def __invert__(self):
        def not_func(*args, **kwargs):
            return not self.func(*args, **kwargs)

        return __class__(not_func)


class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        return lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs)

    def __or__(self, other):
        return lambda *args, **kwargs: self(*args, **kwargs) or other(*args, **kwargs)

    def __invert__(self):
        return __class__(lambda *args, **kwargs: not self(*args, **kwargs))
# ========================================
