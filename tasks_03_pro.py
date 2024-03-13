# ======================================== 2.1
def hide_card(card):
    return '*'*12 + ''.join([c for c in card if c.isdigit()])[-4:]


def hide_card(card):
    return '*' * 12 + card.replace(' ', '')[-4:]    


hide_card = lambda c: '*' * 12 + c.replace(' ', '')[-4:]
# ----------------------------------------
def same_parity(lst):
    if lst:
        return list(filter(lambda x: ~(x - lst[0]) % 2, lst))
    else:
        return []


def same_parity(lst):
    return list(filter(lambda x: ~(x - lst[0]) % 2, lst)) if lst else []


def same_parity(nums):
    return [i for i in nums if i % 2 == nums[0] % 2]
# ----------------------------------------
def is_valid(str_: str) -> bool:
    return str_.isdigit() and 4 <= len(str_) <= 6
# ----------------------------------------
def print_given(*args, **kwargs):
    for value, class_ in zip(args, map(type, args)):
        print(value, class_)
    for key, value, class_ in sorted(zip(kwargs.keys(), kwargs.values(), map(type, kwargs.values()))):
        print(key, value, class_)


def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))
    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))
# ----------------------------------------
import string
def convert(str_):
    sum_lower = sum([1 for c in str_ if c in string.ascii_lowercase])
    sum_upper = sum([1 for c in str_ if c in string.ascii_uppercase])
    return str_.upper() if sum_upper > sum_lower else str_.lower()


import string
def convert(str_):
    sum_ = sum([1 if c in string.ascii_lowercase else (-1 if c in string.ascii_uppercase else 0) for c in str_])
    return str_.lower() if sum_ >= 0 else str_.upper()    


def convert(string):
    return string.upper() if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0 else string.lower()


def convert(text):
    lower_count = len(list(filter(str.islower, text)))
    upper_count = len(list(filter(str.isupper, text)))
    if lower_count >= upper_count:
        return text.lower()
    return text.upper()    
# ----------------------------------------
def get_dict(str_):
    dict_ = {}
    for c in str_:
        dict_[c] = dict_.get(c, 0) + 1
    return dict_
def filter_anagrams(str_, lst):
    return [word for word in lst if get_dict(str_) == get_dict(word)]


def filter_anagrams(word, anagrams):
    return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]
# ----------------------------------------
def likes(lst):
    if not lst:
        return 'Никто не оценил данную запись'
    elif len(lst) == 1:
        return f'{lst[0]} оценил(а) данную запись'
    elif len(lst) == 2:
        return f'{lst[0]} и {lst[1]} оценили данную запись'
    elif len(lst) == 3:
        return f'{lst[0]}, {lst[1]} и {lst[2]} оценили данную запись'
    else:
        return f'{lst[0]}, {lst[1]} и {len(lst) - 2} других оценили данную запись'
# ----------------------------------------
def index_of_nearest(lst, num):
    if not lst:
        return -1
    else:
        lst = list(map(lambda x: abs(x - num), lst))
        return lst.index(min(lst))


def index_of_nearest(nums, n):
    if nums:
        minimum = min(nums, key=lambda num: abs(num - n))
        return nums.index(minimum)
    return -1
# ----------------------------------------
def spell(*args):
    dict_ = {}
    for word in map(str.lower, args):
        dict_[word[0]] = max(dict_.get(word[0], 0), len(word))
    return dict_
# ----------------------------------------
# рубль-рубля-рублей
def choose_plural(amount, declensions):
    if 11 <= amount % 100 <= 19:
        return f'{amount} {declensions[2]}'
    elif amount % 10 == 1:
        return f'{amount} {declensions[0]}'
    elif amount % 10 in [2, 3, 4]:
        return f'{amount} {declensions[1]}'
    elif amount % 10 in [5, 6, 7, 8, 9, 0]:
        return f'{amount} {declensions[2]}'
# ----------------------------------------
def get_biggest(list_):
    if list_:
        list_sorted = sorted(map(lambda x: (x*5, len(x)), map(str, list_)), reverse=True)
        return int(''.join([el[0][:el[1]] for el in list_sorted]))
    else:
        return -1


def get_biggest(list_):
    if list_:
        return int(''.join(sorted(map(str, list_), key=lambda x: x*5, reverse=True)))
    return -1
# ======================================== 2.2
def shortest(list_):
    dist = min(list_[:2])
    dist += min(sum(list_[:2]), list_[2])
    dist += min(max(list_[:2]), dist)
    return dist
list_ = [int(input()) for _ in range(3)]
print(shortest(list_))
# ----------------------------------------
set_ = {'en' if input() in 'AaBCcEeHKMOoPpTXxy' else 'ru' for _ in range(3)}
print('mix') if len(set_) == 2 else print(*set_)
# ----------------------------------------
def func(n, x, y, a, b):
    l = list(range(1, n + 1))
    l = l[:x-1] + list(reversed(l[x-1: y])) + l[y:]
    l = l[:a-1] + list(reversed(l[a-1: b])) + l[b:]
    print(*l)
args = map(int, input().split())
func(*args)


def func(n, x, y, a, b):
    l = list(range(1, n + 1))
    l[x-1: y] = reversed(l[x-1: y])
    l[a - 1: b] = reversed(l[a-1: b])
    print(*l)
args = map(int, input().split())
func(*args)
# ----------------------------------------
def func(*args):
    dict_ = {}
    for c in args:
        dict_[c] = dict_.get(c, 0) + 1
    print(*sorted(key for key, value in dict_.items() if value > 1))
args = map(int, input().split())
func(*args)


nums = [int(i) for i in input().split()]
print(*sorted(filter(lambda i: nums.count(i)    > 1, set(nums))))
# ----------------------------------------
def func(n):
    list_ = list(range(1, n + 1))
    dict_ = {}
    for el in list_:
        key = sum(map(int, list(str(el))))
        dict_[key] = dict_.get(key, 0) + 1
    print(max(dict_.values()))
func(int(input()))
# ----------------------------------------
def func(list_):
    intersection = sorted(set.intersection(*list_))
    print(*intersection, sep=', ') if intersection else print('Сериал снять не удастся')
list_ = [set(input().split(', ')) for _ in range(int(input()))]
func(list_)
# ----------------------------------------
def func(word, words):
    vowels = 'ауоыиэяюёе'
    word_indexes = [ind for ind, c in enumerate(word) if c in vowels]
    words_indexes = [[ind for ind, c in enumerate(word) if c in vowels] for word in words]
    [print(words[ind]) for ind, word_indexes_2 in enumerate(words_indexes) if word_indexes_2 == word_indexes]
word = input()
words = [input() for _ in range(int(input()))]
func(word, words)


vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
pattern = [i for i, c in enumerate(input()) if c in vowels]
for _ in range(int(input())):
    word = input()
    if [i for i, c in enumerate(word) if c in vowels] == pattern:
        print(word)
# ----------------------------------------
occupied = [input().split('@')[0] for _ in range(int(input()))]
dict_ = {}
for name in occupied:
    ind = [ind for ind, c in enumerate(name) if c.isdigit()]
    if ind:
        dict_[name[:min(ind)]] = dict_.get(name[:min(ind)], set()) | {int(name[ind[0]:])}
    else:
        dict_[name] = dict_.get(name, set()) | {0}
unoccupied = [input() for _ in range(int(input()))]
for name in unoccupied:
    set_ = dict_.get(name, set())
    for i in range(100):
        if i in set_:
            continue
        else:
            dict_[name] = dict_.get(name, set()) | {i}
            if i == 0:
                print(name + '@beegeek.bzz')
            else:
                print(name + str(i) + '@beegeek.bzz')
            break


occupied = [input().split('@')[0] for _ in range(int(input()))]
dict_ = {}
for name in occupied:
    ind = [ind for ind, c in enumerate(name) if c.isdigit()]
    if ind:
        dict_[name[:min(ind)]] = dict_.get(name[:min(ind)], set()) | {int(name[ind[0]:])}
    else:
        dict_[name] = dict_.get(name, set()) | {0}
unoccupied = [input() for _ in range(int(input()))]
for name in unoccupied:
    set_ = dict_.get(name, set())
    i = 0
    while True:
        if i in set_:
            i += 1
            continue
        else:
            dict_[name] = dict_.get(name, set()) | {i}
            print(name + '@beegeek.bzz') if i == 0 else print(name + str(i) + '@beegeek.bzz')
            break


digits, names = '0123456789', []
for _ in range(int(input())):
    name, _ = input().split('@')
    names.append(name)
for _ in range(int(input())):
    name = input()
    counter = 1
    while name in names:
        name = name.rstrip(digits) + str(counter)
        counter += 1
    names.append(name)
    print(f'{name}@beegeek.bzz')
# ----------------------------------------
import math
def max_size(size):
    """Принимает число в байтах и возвращает число в B, KB, MB, GB"""
    unit_names = ('B', 'KB', 'MB', 'GB', 'TB')
    pwr = math.floor(math.log(size, 1024))
    return round(size / 1024 ** pwr), unit_names[pwr]


def max_size(size, degree=1024, iters=None):
    if iters is None:
        iters = ['B', 'KB', 'MB', 'GB', 'TB']
    iter_ = -1
    while size >= 1:
        round_size = round(size)
        size /= degree
        iter_ += 1
    return round_size, iters[iter_]

with open('files.txt', mode='r+', encoding='UTF-8') as f:
    list_ = f.readlines()
list_ = [*map(str.split, [string.replace('.', ' ') for string in list_])]
list_sorted = sorted(list_, key=lambda x: x[0])  # filename
list_sorted = sorted(list_sorted, key=lambda x: x[1])  # extantion

ext = list_sorted[0][1]
size = 0
bites = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3, 'TB': 1024 ** 4}
for el in list_sorted:
    if el[1] == ext:
        size += int(el[2]) * bites[el[3]]
        print(f'{el[0]}.{el[1]}')
    else:
        print('----------')
        print('Summary:', *max_size(size))
        print()
        ext = el[1]
        size = int(el[2]) * bites[el[3]]
        print(f'{el[0]}.{el[1]}')
print('----------')
print('Summary:', *max_size(size))
# ======================================== 3.1
# импортируем тип date из модуля datetime
from datetime import date

# выводим текущую дату
print(date.today())
# ----------------------------------------
# импортируем тип date из модуля datetime
from datetime import date

# создаем объект, соответсвующий дате урагана
hurricane_andrew = date(1992, 8, 24)

# выводим день недели
print(hurricane_andrew.weekday())
# ----------------------------------------
# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)
# ----------------------------------------
from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

for date in dates:
    print(f'{date.year}-Q{(date.month - 1) // 3 + 1}')
# ----------------------------------------
from datetime import date
def get_min_max(args):
    return (min(args), max(args)) if args else tuple()

dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))
# ----------------------------------------
from datetime import date
def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]


from datetime import date
def get_date_range(date1, date2):
    l = []
    while date2 >= date1:
        l.append(date1)
        date1 = date.fromordinal(date1.toordinal() + 1)
    return l
# ----------------------------------------
from datetime import date
def saturdays_between_two_dates(date1, date2):
    start = min(date1, date2)
    end = max(date1, date2)
    return sum([date.fromordinal(d).weekday() == 5 for d in range(start.toordinal(), end.toordinal() + 1)])


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    return sum([date.fromordinal(d).weekday() == 5 for d in range(start.toordinal(), end.toordinal() + 1)])
# ======================================== 3.2
from datetime import time
alarm = time(7, 30, 25)
print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.strftime('%M'))
print('Секунды:', alarm.strftime('%S'))
# ----------------------------------------
from datetime import date
birthday = date(1992, 10, 6)
print('Название месяца:', birthday.strftime('%B'))
print('Название дня недели:', birthday.strftime('%A'))
print('Год:', birthday.strftime('%Y'))
print('Месяц:', birthday.strftime('%m'))
print('День:', birthday.strftime('%d'))
# ----------------------------------------
# присваиваем самую раннюю дату урагана в переменную first_date
first_date = min(florida_hurricane_dates)
# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')
print(iso)
print(ru)
print(us)
# ----------------------------------------
from datetime import date
andrew = date(1992, 8, 24)
print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number
# ----------------------------------------
from datetime import date
print(min([date.fromisoformat(input()) for _ in range(2)]).strftime('%d-%m (%Y)'))
# ----------------------------------------
from datetime import date
print(*[d.strftime('%d/%m/%Y') for d in sorted([date.fromisoformat(input()) for _ in range(int(input()))])], sep='\n')

dates = [date.fromisoformat(input()) for _ in range(int(input()))]
for d in sorted(dates):
    print(d.strftime('%d/%m/%Y'))
# ----------------------------------------
from datetime import date
def print_good_dates(dates):
    for d in sorted([d for d in dates if d.year == 1992 and d.day + d.month == 29]):
        print(d.strftime('%B %d, %Y'))
# ----------------------------------------
from datetime import date
def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except:
        return False


from datetime import date
def is_correct(*args):
    try:
        return bool(date(*args[::-1]))
    except:
        return False
# ----------------------------------------
from datetime import date
def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except:
        return False
dates = []
d = input()
while d != 'end':
    dates.append('Корректная' if is_correct(*map(int, d.split('.'))) else 'Некорректная')
    d = input()
print(*dates, dates.count('Корректная'), sep='\n')
# ======================================== 3.3
from datetime import datetime
text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
dt = datetime.strptime(text, 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M')
print(dt)
# ----------------------------------------
from datetime import datetime
seconds = 2483228800
dt = datetime(2011, 11, 4)
print(datetime.fromtimestamp(seconds))
print(dt.timestamp())
# ----------------------------------------
from datetime import datetime
times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), 
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), 
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53), 
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3), 
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5), 
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54), 
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45), 
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57), 
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42), 
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12), 
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27), 
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41), 
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44), 
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]
print('После полудня' if sum(1 if p.hour >= 12 else -1 for p in times_of_purchases) else 'До полудня')


dts = [d.strftime('%p') for d in times_of_purchases]
print(['До полудня', 'После полудня'][dts.count('PM')>dts.count('AM')])
# ----------------------------------------
from datetime import date, time, datetime
dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24), 
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59), 
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2), 
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
print(*sorted([datetime.combine(d, t) for d, t in zip(dates, times)], key=lambda dt: dt.strftime('%S')), sep='\n')


print(*sorted([datetime.combine(d, t) for d, t in zip(dates, times)], key=lambda dt: dt.second), sep='\n')
# ----------------------------------------
from datetime import datetime
data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}
spent_time = 10**10
format_ = '%d.%m.%Y %H:%M:%S'
for key, value in data.items():
    delta = datetime.strptime(value[1], format_).timestamp() - datetime.strptime(value[0], format_).timestamp()
    if delta < spent_time:
        name = key
        spent_time = delta
print(name)


for key, value in data.items():
    dt1 = datetime.strptime(value[0], '%d.%m.%Y %H:%M:%S').timestamp()
    dt2 = datetime.strptime(value[1], '%d.%m.%Y %H:%M:%S').timestamp()
    data[key] = dt2 - dt1
print(min(data, key=data.get))
# print(min(data.keys(), key=data.get))
# ----------------------------------------
from datetime import date, time, datetime
with open('diary.txt', mode='r+', encoding='UTF-8') as f:
    list_ = f.readlines()
format_ = '%d.%m.%Y; %H:%M'
dict_ = {}
for string in list_:
    try:
        datetime_key = datetime.strptime(string.rstrip(), format_)
        dict_[datetime_key] = dict_.get(datetime_key, list())
    except ValueError:
        if string.rstrip():
            dict_[datetime_key].append(string.rstrip())
for key, value in sorted(dict_.items()):
    print(key.strftime('%d.%m.%Y; %H:%M'))
    print(*value, sep='\n')
    print()


# my_2
from datetime import date, time, datetime
with open('diary.txt', mode='r+', encoding='UTF-8') as file:
    list_ = file.read().split('\n\n')
pattern = '%d.%m.%Y; %H:%M'
for string in sorted(list_, key=lambda x: datetime.strptime(x[:17], pattern)):
    print(*string.split('\n', 1), sep='\n')
    print()
--------------------
from datetime import datetime
notes = {}
pattern = '%d.%m.%Y; %H:%M'
with open('diary.txt', encoding='utf-8') as file:
    diary = file.read().split('\n\n')
    for note in diary:
        dt, text = note.split('\n', 1)
        dt = datetime.strptime(dt, pattern)
        notes[dt] = text
for dt, text in sorted(notes.items()):
    print(dt.strftime(pattern))
    print(text)
    print()


from datetime import datetime
with open('diary.txt', 'r', encoding='utf-8') as diary:
    diary = sorted(diary.read().split('\n\n'), key=lambda d: datetime.strptime(d[0:17], '%d.%m.%Y; %H:%M'))
print(*diary, sep='\n\n')    
# ----------------------------------------
from datetime import datetime as dt
pattern = '%d.%m.%Y'
day_sec = 86400
def is_available_date(booked_dates, dates_for_booking):
    booked_set, for_booking_set = set(), set()
    for dates in booked_dates:
        booked_set |= set(range(int(dt.strptime(dates[:10], pattern).timestamp()), int(dt.strptime(dates[-10:], pattern).timestamp()) + day_sec, day_sec))
    for_booking_set |= set(range(int(dt.strptime(dates_for_booking[:10], pattern).timestamp()), int(dt.strptime(dates_for_booking[-10:], pattern).timestamp()) + day_sec, day_sec))
    return not bool(booked_set & for_booking_set)

# my_2
from datetime import datetime as dt
def to_ordinal(date_, pattern='%d.%m.%Y'):
    return int(dt.strptime(date_, pattern).toordinal())
def is_available_date(booked_dates, dates_for_booking):
    booked_set, for_booking_set = set(), set()
    for dates in booked_dates:
        booked_set |= set(range(to_ordinal(dates[:10]), to_ordinal(dates[-10:]) + 1))
    for_booking_set |= set(range(to_ordinal(dates_for_booking[:10]), to_ordinal(dates_for_booking[-10:]) + 1))
    return not bool(booked_set & for_booking_set)
# ======================================== 3.4
from datetime import datetime, timedelta
dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)
print(dt.strftime('%d.%m.%Y %H:%M:%S'))
# ----------------------------------------
from datetime import date, timedelta
today = date(2021, 11, 4)
birthday = date(2022, 10, 6)
days = (birthday - today).days
print(days)
# ----------------------------------------
from datetime import date, datetime, timedelta
pattern = '%d.%m.%Y'
date_cur = datetime.strptime(input(), pattern)
print((date_cur + timedelta(days=-1)).strftime(pattern),
      (date_cur + timedelta(days=1)).strftime(pattern), sep='\n')


from datetime import date, datetime, timedelta
pattern = '%d.%m.%Y'
td = timedelta(days=1)
dt = datetime.strptime(input(), pattern)
print((dt - td).strftime(pattern))
print((dt + td).strftime(pattern))
# ----------------------------------------
from datetime import date, time, datetime, timedelta
t = datetime.strptime(input(), '%H:%M:%S')
print(int(timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()))
# ----------------------------------------
from datetime import date, time, datetime, timedelta
pattern = '%H:%M:%S'
print((datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))).strftime(pattern))
# ----------------------------------------
from datetime import date, time, datetime, timedelta
def num_of_sundays(year):
    dt1 = datetime(year=year, month=1, day=1).toordinal()
    dt2 = datetime(year=year, month=12, day=31).toordinal()
    return sum([datetime.fromordinal(dt).strftime('%w') == '0' for dt in range(dt1, dt2 + 1)])
from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
def fill_up_missing_dates(dates):
    l = [datetime.strptime(i, pattern) for i in dates]
    dt1 = datetime(year=min(l).year, month=min(l).month, day=min(l).day).toordinal()
    dt2 = datetime(year=max(l).year, month=max(l).month, day=max(l).day).toordinal()
    return [datetime.fromordinal(dt).strftime(pattern) for dt in range(dt1, dt2 + 1)]

from datetime import datetime
def num_of_sundays(year):
    dt = datetime(year, 12, 31)
    return int(dt.strftime('%U'))
# ----------------------------------------
from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern)
for i in range(10):
    dt += timedelta(days=i + int(i > 0))
    print(dt.strftime(pattern))


...
for i in range(10):
    print(dt.strftime(pattern))
    dt += timedelta(days=i + 2)
# ----------------------------------------
from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
l = [datetime.strptime(dt, pattern) for dt in input().split()]
l_res = []
if len(l) > 1:
    for i in range(len(l) - 1):
        l_res.append((max(l[i], l[i+1]) - min(l[i], l[i+1])).days)
print(l_res)


from datetime import date, time, timedelta, datetime
dates = [datetime.strptime(dt, '%d.%m.%Y') for dt in input().split()]
diffs = [abs(dates[i] - dates[i-1]).days for i in range(1, len(dates))]
print(diffs)
# ----------------------------------------
from datetime import date, time, datetime, timedelta
def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    dt_list = [datetime.strptime(i, pattern) for i in dates]
    return [datetime.fromordinal(dt).strftime(pattern) for dt in range(min(dt_list).toordinal(), max(dt_list).toordinal() + 1)]


def fill_up_missing_dates(dates):
    pattern = '%d.%m.%Y'
    dates = [datetime.strptime(d, pattern) for d in dates]
    start, end = min(dates), max(dates)
    days = (end - start).days
    return [(start + timedelta(days=i)).strftime(pattern) for i in range(days + 1)]
# ----------------------------------------
from datetime import date, time, datetime, timedelta
pattern = '%H:%M'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)
while end - start >= timedelta(minutes=45):
    print(start.strftime(pattern), (start + timedelta(minutes=45)).strftime(pattern), sep=' - ')
    start += timedelta(minutes=55)
# ======================================== 3.5
from datetime import date, time, datetime, timedelta
data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
pattern = '%H:%M'
print(int(sum([(datetime.strptime(dt[1], pattern) - datetime.strptime(dt[0], pattern)).total_seconds() // 60 for dt in data])))
# ----------------------------------------
from datetime import date, time, datetime, timedelta
l = []
for year in range(1, 10000):
    for month in range(1, 13):
        l.append(datetime(year=year, month=month, day=13).strftime('%w'))
for day in [1, 2, 3, 4, 5, 6, 0]:
    print(l.count(str(day)))
# ----------------------------------------
from datetime import date, time, datetime, timedelta
timetable = [('09:00', '21:00'),
             ('09:00', '21:00'),
             ('09:00', '21:00'),
             ('09:00', '21:00'),
             ('09:00', '21:00'),
             ('10:00', '18:00'),
             ('10:00', '18:00')]
pattern_day = '%d.%m.%Y %H:%M'
pattern_time = '%H:%M'
dt = datetime.strptime(input(), pattern_day)
weekday = dt.weekday()
start = datetime.strptime(timetable[weekday][0], pattern_time)
end = datetime.strptime(timetable[weekday][1], pattern_time)
cur_time = datetime(1900, 1, 1, hour=dt.hour, minute=dt.minute)
if start <= cur_time < end:
    print((end - cur_time).seconds // 60)
else:
    print('Магазин не работает')
# ----------------------------------------
from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
start, end = datetime.strptime(input(), pattern), datetime.strptime(input(), pattern)
def func(dt):
    dt = datetime.fromordinal(dt)
    if dt.isoweekday() not in (1, 4):
        return dt.strftime(pattern)
while start <= end:
    if (start.month + start.day) % 2 == 1:
        break
    start += timedelta(days=1)
print(*filter(lambda x: x, [func(dt) for dt in range(start.toordinal(), end.toordinal() + 1, 3)]), sep='\n')


from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
start, end = [datetime.strptime(input(), pattern) for _ in range(2)]
while (start.month + start.day) % 2 == 0:
    start += timedelta(days=1)
while start <= end:
    if start.isoweekday() not in (1, 4):
        print(start.strftime(pattern))
    start += timedelta(days=3)
# ----------------------------------------
from datetime import date, time, datetime, timedelta
list_ = [s.split() for s in [input() for _ in range(int(input()))]]
min_ = min(list_, key=lambda x: datetime.strptime(x[2], '%d.%m.%Y'))
sum_ = sum([min_[2] in i[2] for i in list_])
if sum_ > 1:
    print(min_[2], sum_)
else:
    print(min_[2], min_[0], min_[1])
# ----------------------------------------
from datetime import date, time, datetime, timedelta
dict_ = {}
pattern = '%d.%m.%Y'
list_ = [s.split() for s in [input() for _ in range(int(input()))]]
for i in list_:
    key = datetime.strptime(i[2], pattern)
    dict_[key] = dict_.get(key, 0) + 1
print(*[key.strftime(pattern) for key, value in sorted(dict_.items()) if value == max(dict_.values())], sep='\n')
# ----------------------------------------
from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern)
list_ = [s.split() for s in [input() for _ in range(int(input()))]]
list_sorted = []
for i in sorted(list_, key=lambda x: datetime.strptime(x[2], pattern)):
    if ((dt < datetime.strptime(i[2], pattern).replace(year=dt.year) <= dt + timedelta(days=7)) or
            (dt < datetime.strptime(i[2], pattern).replace(year=dt.year + 1) <= dt + timedelta(days=7))):
        list_sorted.append(i[:2])
print(*list_sorted[-1]) if list_sorted else print('Дни рождения не планируются')


# str.rsplit(' ', 1)
from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
dt = datetime.strptime(input(), pattern)
list_ = [s.rsplit(' ', 1) for s in [input() for _ in range(int(input()))]]
list_sorted = []
for i in sorted(list_, key=lambda x: datetime.strptime(x[1], pattern)):
    if ((dt < datetime.strptime(i[1], pattern).replace(year=dt.year) <= dt + timedelta(days=7)) or
            (dt < datetime.strptime(i[1], pattern).replace(year=dt.year + 1) <= dt + timedelta(days=7))):
        list_sorted.append(i[0])
print(list_sorted[-1]) if list_sorted else print('Дни рождения не планируются')
# ----------------------------------------
from datetime import date, time, datetime, timedelta

def choose_plural(amount, declensions):
    if 11 <= amount % 100 <= 19:
        return f'{amount} {declensions[2]}'
    elif amount % 10 == 1:
        return f'{amount} {declensions[0]}'
    elif amount % 10 in [2, 3, 4]:
        return f'{amount} {declensions[1]}'
    elif amount % 10 in [5, 6, 7, 8, 9, 0]:
        return f'{amount} {declensions[2]}'

pattern = '%d.%m.%Y %H:%M'
release = datetime.strptime('08.11.2022 12:00', pattern)
date_ = datetime.strptime(input(), pattern)
delta_ = release - date_
if delta_.total_seconds() <= 0:
    print('Курс уже вышел!')
elif delta_.days:
    print('До выхода курса осталось:',
          f'{choose_plural(delta_.days, ["день", "дня", "дней"])}',
          f'и {choose_plural(delta_.seconds // 3600, ["час", "часа", "часов"])}' if delta_.seconds // 3600 > 0 else '')
elif delta_.seconds // 3600 > 0:
    print('До выхода курса осталось:',
          f'{choose_plural(delta_.seconds // 3600, ["час", "часа", "часов"])}',
          f'и {choose_plural(delta_.seconds % 3600 // 60, ["минута", "минуты", "минут"])}' if delta_.seconds % 3600 // 60 > 0 else '')
elif delta_.seconds // 3600 == 0:
    print('До выхода курса осталось:',
          f'{choose_plural(delta_.seconds % 3600 // 60, ["минута", "минуты", "минут"])}')
# ======================================== 3.6
import time
def calculate_it(func, *args):
    start = time.perf_counter()
    res = func(*args)
    end = time.perf_counter()
    return res, end - start
# ----------------------------------------
import time
def get_the_fastest_func(funcs, arg):
    list_ = []
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        list_.append(end - start)
    return funcs[list_.index(min(list_))]
def add(a):
    return a + a
def mult(a):
    return a ** a
print(get_the_fastest_func([add, mult], arg=2))


import timeit
def get_the_fastest_func(funcs, arg):
    return min({timeit.timeit(lambda: func(arg), number=1): func for func in funcs}.items())[1]


import timeit
def get_the_fastest_func(funcs, arg):
    return min(((timeit.timeit(lambda: func(arg), number=1), func) for func in funcs))[1]

# timeit example
mysetup = 'from math import sqrt'
mycode = '''
mylist = []
for i in range(100):
    mylist.append(sqrt(i))
'''
timeit.timeit(stmt = mycode,
              setup = mysetup,
              number = 10000)
# ======================================== 3.7
import calendar
print(*[calendar.isleap(int(input())) for _ in range(int(input()))], sep='\n')
# ----------------------------------------
import calendar
args = input().split()
calendar.prmonth(int(args[0]), list(calendar.month_abbr).index(args[1]))


from calendar import prmonth
from datetime import datetime
dt = datetime.strptime(input(), '%Y %b')
prmonth(dt.year, dt.month)
# ----------------------------------------
import calendar, datetime
dt = datetime.datetime.strptime(input(), '%Y-%m-%d')
print(calendar.day_name[calendar.weekday(dt.year, dt.month, dt.day)])


from datetime import datetime
print(datetime.strptime(input(), '%Y-%m-%d').strftime('%A'))
# ----------------------------------------
import calendar, datetime
dt = datetime.datetime.strptime(input(), '%Y %m')
print(calendar.monthrange(dt.year, dt.month)[1])
# ----------------------------------------
import calendar, datetime
dt = datetime.datetime.strptime(input(), '%Y %B')
print(calendar.monthrange(dt.year, dt.month)[1])
# ----------------------------------------
import calendar, datetime
def get_days_in_month(year, month):
    month_ind = list(calendar.month_name).index(month)
    return [datetime.date(year, month_ind, day) for day in range(1, calendar.monthrange(year, month_ind)[1] + 1)]
# ----------------------------------------
import calendar, datetime
def get_all_mondays(year):
    dt_start = datetime.datetime(year=year, month=1, day=1)
    dt_end = datetime.datetime(year=year, month=12, day=31)
    while dt_start.weekday() != 0:
        dt_start += datetime.timedelta(days=1)
    return [datetime.date.fromordinal(day) for day in range(dt_start.toordinal(), dt_end.toordinal() + 1, 7)]
# ----------------------------------------
import calendar, datetime
def free_museum(year):
    dt_start = datetime.datetime(year=year, month=1, day=1)
    dt_end = datetime.datetime(year=year, month=12, day=31)
    dict_ = {}
    while dt_start <= dt_end:
        if dt_start.weekday() == 3:
            dict_[dt_start.month] = dict_.get(dt_start.month, []) + [dt_start]
        dt_start += datetime.timedelta(days=1)
    return [value[2].strftime('%d.%m.%Y') for value in dict_.values()]
print(*free_museum(int(input())), sep='\n')


from calendar import weekday, THURSDAY
from datetime import datetime
year = int(input())
for month in range(1, 13):
    for day in range(15, 22):
        if weekday(year, month, day) == THURSDAY:
            thursday = datetime(year, month, day)
            print(thursday.strftime('%d.%m.%Y'))
            break
# ======================================== 4.1
import sys
for line in sys.stdin:
    print(line.strip('\n')[::-1])
# ----------------------------------------
import sys, datetime
list_ = [datetime.datetime.strptime(line.strip('\n'), '%Y-%m-%d') for line in sys.stdin]
print((max(list_) - min(list_)).days)


import sys
from datetime import datetime
date = [datetime.fromisoformat(i.strip()) for i in sys.stdin]
print((max(date) - min(date)).days)
# ----------------------------------------
import sys
PLAYERS = ('Анри', 'Дима')
list_ = [int(line.strip('\n')) for line in sys.stdin]
if list_[-1] % 2:
    print(PLAYERS[len(list_) % 2])
else:
    print(PLAYERS[(len(list_) + 1) % 2])


import sys
list_ = [int(line.strip('\n')) for line in sys.stdin]
print('Анри' if (len(list_) + list_[-1]) % 2 == 1 else 'Дима')
# ----------------------------------------
import sys, numpy as np
list_ = [int(line) for line in sys.stdin]
if list_:
    print(f'Рост самого низкого ученика: {min(list_)}')
    print(f'Рост самого высокого ученика: {max(list_)}')
    print(f'Средний рост: {np.mean(list_)}')
else:
    print('нет учеников')
# ----------------------------------------
import sys
list_ = [line.strip() for line in sys.stdin]
print(len(list(filter(lambda s: s.startswith('#'), list_))))


import sys
print(sum(line.strip().startswith('#') for line in sys.stdin))
# ----------------------------------------
import sys
print(*list(filter(lambda s: not s.strip().startswith('#'), sys.stdin.readlines())), sep='')


import sys
for line in sys.stdin:
    if not line.lstrip().startswith('#'):
        print(line.rstrip())
# ----------------------------------------
import sys
list_ = [line.strip('\n') for line in sys.stdin]
category = list_[-1]
news = [n.split(' / ') for n in list_[:-1]]
news = filter(lambda n: n[1] == category, news)
news = sorted(news, key=lambda n: (float(n[2]), n[0]))
print(*[n[0] for n in news], sep='\n')
# ----------------------------------------
import sys, datetime
list_ = [datetime.datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
if len(list_) > len(set(list_)):
    print('MIX')
elif list_ == sorted(list_):
    print('ASC')
elif list_ == sorted(list_, reverse=True):
    print('DESC')
else:
    print('MIX')
# ----------------------------------------
import sys
list_ = [int(line) for line in sys.stdin]
if len(set([m - n for n, m in zip(list_[:-1], list_[1:])])) == 1:
    print('Арифметическая прогрессия')
elif len(set([m / n for n, m in zip(list_[:-1], list_[1:])])) == 1:
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
# ======================================== 4.2
import csv
with open('grades.csv', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for line in reader:
        print(line)
# ----------------------------------------
import csv
with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'])
    writer.writeheader()
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})
# ----------------------------------------
import csv
with open('sales.csv', encoding='utf-8', newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for line in reader:
        if int(line['new_price']) < int(line['old_price']):
            print(line['name'])
# ----------------------------------------
import csv
import numpy as np
with open('salary_data.csv', encoding='utf-8', newline='') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    dict_ = {}
    for line in reader:
        dict_[line['company_name']] = dict_.get(line['company_name'], []) + [int(line['salary'])]
    dict_ = [(np.mean(v), k) for k, v in dict_.items()]
    dict_.sort()
    print(*[i[1] for i in dict_], sep='\n')


import pandas as pd
df = pd.read_csv('salary_data.csv', sep=';')
df = df.groupby(['company_name'], as_index=False).mean()
df.sort_values(by=['salary', 'company_name'], inplace=True)
print(*list(df['company_name']), sep='\n')


import pandas as pd
df = pd.read_csv('salary_data.csv', sep=';')
df = df.groupby(by=['company_name']).mean().sort_values(by=['salary', 'company_name'])
print(*df.index.tolist(), sep='\n')


import csv
d = {}
with open('salary_data.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    for key, value in rows[1:]:
        d[key] = d.get(key, []) + [int(value)]
    d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
    print(*d_sort, sep='\n')
# ----------------------------------------
import csv
with open('deniro.csv', encoding='utf-8', newline='') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=','))
col = int(input())
rows.sort(key=lambda x: (str, int, int)[col - 1](x[col - 1]))
for row in rows:
    print(*row, sep=',')


# не соасем верная сортировка
import pandas as pd
df = pd.read_csv('deniro.csv', sep=',', names=[1, 2, 3])
df = df.sort_values(by=2)
for v in df.values:
    print(*v, sep=',')
# ----------------------------------------
import pandas as pd
def csv_columns(filename):
    df = pd.read_csv(filename, sep=',', dtype=str)
    dict_ = {}
    for col in df.columns:
        dict_[col] = df[col].values.tolist()
    return dict_


import pandas as pd
def csv_columns(filename):
    return pd.read_csv(filename).astype(str).to_dict(orient='list')


import csv
def csv_columns(filename):
    with open(filename, encoding="utf-8") as file_in:
        rows = list(csv.reader(file_in))
        return {key: value for key, *value in zip(*rows)}
# ----------------------------------------
import csv
with open('data.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file))
    dict_ = {}
    for line in rows[1:]:
        key = line[2].split('@')[1]
        dict_[key] = dict_.get(key, 0) + 1
with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['domain', 'count'])
    for row in sorted(dict_.items(), key=lambda x: (dict_[x[0]], x[0])):
#   for row in sorted(dict_.items(), key=lambda x: (x[1], x[0])):
        writer.writerow(row)
# ----------------------------------------
import csv
with open('wifi.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=';'))
    dict_ = {}
    for line in rows[1:]:
        dict_[line[1]] = dict_.get(line[1], 0) + int(line[3])
    dict_ = sorted(dict_.items())
    for k, v in sorted(dict_, key=lambda x: x[1], reverse=True):
        print(f'{k}: {v}')


import csv
with open('wifi.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=';'))
    dict_ = {}
    for line in rows[1:]:
        dict_[line[1]] = dict_.get(line[1], 0) + int(line[3])
    for k, v in sorted(dict_.items(), key=lambda x: (-x[1], x[0])):
        print(f'{k}: {v}')
# ----------------------------------------
import csv
with open('titanic.csv', encoding='utf-8') as csv_file:
    rows = list(csv.reader(csv_file, delimiter=';'))
    for line in sorted(rows[1:], key=lambda x: x[2], reverse=True):
        if float(line[3]) < 18 and line[0] == '1':
            print(line[1])


import pandas as pd
df = pd.read_csv('titanic.csv', delimiter=';')
df_new = df.loc[(df.age < 18) & (df.survived == 1)]
print(*df_new.loc[df.sex == 'male'].name, sep='\n')
print(*df_new.loc[df.sex == 'female'].name, sep='\n')


import csv
with open('titanic.csv', encoding='utf-8') as f:
    passengers = [d for  s, *d, a in csv.reader(f, delimiter=';') if s == '1' and float(a) < 18]
[print(name) for name, _ in sorted(passengers, key=lambda x: x[1], reverse=True)]  
# ----------------------------------------
import csv, datetime
with open('name_log.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=','))
    dict_ = {}
    for line in rows[1:]:
        dict_[line[1]] = dict_.get(line[1], []) + [(line[0], datetime.datetime.strptime(line[2], '%d/%m/%Y %H:%M'))]
with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
    writer.writerow(['username', 'email', 'dtime'])
    for k, v in sorted(dict_.items()):
        v_sorted = sorted(v, key=lambda x: x[1], reverse=True)
        writer.writerow((v_sorted[0][0], k, datetime.datetime.strftime(v_sorted[0][1], '%d/%m/%Y %H:%M')))


import csv
from datetime import datetime
with open('name_log.csv', encoding='UTF-8') as f:
    header, *rows = csv.reader(f)
d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}
with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(sorted(d.values(), key=lambda x: x[1]))
# ----------------------------------------
import csv
def condense_csv(filename, id_name='ID'):
    with open(filename, encoding='utf-8') as file:
        rows = list(csv.reader(file, delimiter=','))
        dict_obj = {}
        columns = []
        for row in rows:
            dict_obj[row[0]] = dict_obj.get(row[0], {}) | {row[1]: row[2]}
            if row[1] not in columns:
                columns.append(row[1])
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
        writer.writerow([id_name, *columns])
        for key, value in dict_obj.items():
            row_new = [key]
            for col in columns:
                row_new.append(value[col])
            writer.writerow(row_new)


import csv
def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as file:
        objects = {}
        for obj, attr, value in csv.reader(file):
            if obj not in objects:
                objects[obj] = {id_name: obj}
            objects[obj][attr] = value
    with open('condensed.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=objects[obj])
        writer.writeheader()
        writer.writerows(objects.values())
# ----------------------------------------
import csv
with open('student_counts.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=','))
    list_ = list(zip(*[rows[i][1:] for i in range(len(rows))]))
    list_.sort(key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1]))
with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
    writer.writerow(['year', *[el[0] for el in list_]])
    for i in range(1, len(list_[0])):
        writer.writerow([1999+i, *[el[i] for el in list_]])


import csv
def key_func(grade):
    number, letter = grade.split('-')
    return int(number), letter
with open('student_counts.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    columns = ['year'] + sorted(reader.fieldnames[1:], key=key_func)
    rows = list(reader)
with open('sorted_student_counts.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(rows)
# ----------------------------------------
import csv
with open('prices.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    min_price = 1_000_000
    dict_ = {}
    for row in rows[1:]:
        for i in range(1, len(row)):
            if int(row[i]) < min_price:
                min_price = int(row[i])
                dict_[min_price] = dict_.get(min_price, []) + [(rows[0][i], row[0])]
    list_ = list(sorted(dict_.items()))
    print(f'{list_[0][1][0][0]}: {list_[0][1][0][1]}')


import csv
with open('prices.csv', encoding='UTF-8') as f:
    h, *rows = csv.reader(f, delimiter=';')
goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))
print(f'{cheapest[1]}: {cheapest[0]}')
# ======================================== 4.4
import json
countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
             'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
             'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
             'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
json_data = json.dumps(countries, indent=3, separators=(',', ' - '), sort_keys=True)
print(json_data)
# ----------------------------------------
import json
words = {
         frozenset(["tap", "telephone"]): ("tæp", "telifəun"),
         "travel": "trævl",
         ("hello", "world"): ("həˈləʊ", "wɜːld"),
         "moonlight": "muːn.laɪt",
         "sunshine": "ˈsʌn.ʃaɪn",
         ("why", "is", "so", "difficult"): ("waɪ", "ɪz", "səʊ", "ˈdɪfɪkəlt"),
         "adventure": "ədˈventʃər",
         "beautiful": "ˈbjuːtɪfl",
         frozenset(["spoon", "block"]): ("spu:n", "blɔk"),
         "bicycle": "baisikl",
         ("pilot", "fly"): ("pailət", "flai")
        }
data_json = json.dumps(words, skipkeys=True)
# ----------------------------------------
import json
club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
         "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}
club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
         "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}
club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
         "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}
data = [club1, club2, club3]
with open('data.json', 'w') as file:
    json.dump(data, file, indent='   ')
# ----------------------------------------
import json
specs = {
         'Модель': 'AMD Ryzen 5 5600G',
         'Год релиза': 2021,
         'Сокет': 'AM4',
         'Техпроцесс': '7 нм',
         'Ядро': 'Cezanne',
         'Объем кэша L2': '3 МБ',
         'Объем кэша L3': '16 МБ',
         'Базовая частота': '3900 МГц'
        }
specs_json = json.dumps(specs, ensure_ascii=False, indent='   ')
print(specs_json)
# ----------------------------------------
import json
def is_correct_json(string):
    try:
        json.loads(string)
        return True
        # return bool(json.loads(string))
    except:
        return False
# ----------------------------------------
import json, sys
text = sys.stdin.read()
data = json.loads(text)
for key, value in data.items():
    if type(value) == list:
  # if isinstance(value, list):
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f'{key}: {value}')
# ----------------------------------------
import json
with open('data.json', encoding='utf8') as file:
    data = json.load(file)
    list_out = []
    for el in data:
        if type(el) == str:
            list_out.append(el + '!')
            continue
        if type(el) == int:
            list_out.append(el + 1)
            continue
        if type(el) == float:
            list_out.append(el + 1)
            continue
        if type(el) == bool:
            list_out.append(not el)
            continue
        if type(el) == list:
            list_out.append(el * 2)
            continue
        if type(el) == dict:
            el["newkey"] = None
            list_out.append(el)
            continue
        if el is None:
            pass
with open('updated_data.json', 'w', encoding='utf8') as file:
    json.dump(list_out, file)


import json
with open('data.json', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8') as new_file:
    data = json.load(file)
    conv_values = {
        str: lambda x: x + '!',
        int: lambda x: x + 1,
        bool: lambda x: not x,
        list: lambda x: x * 2,
        dict: lambda x: {**x, "newkey": None},
    }
    new_data = []
    for d in data:
        if type(d) in conv_values:
            new_data.append(conv_values[type(d)](d))
    json.dump(new_data, new_file, indent=2)
# ----------------------------------------
import json
with open('data1.json', encoding='utf8') as file1, open('data2.json', encoding='utf8') as file2:
    data1, data2 = json.load(file1), json.load(file2)
    data1.update(data2)
with open('data_merge.json', 'w', encoding='utf8') as file:
    json.dump(data1, file)


import json
with open('data1.json', encoding='utf8') as file1, open('data2.json', encoding='utf8') as file2:
    data1, data2 = json.load(file1), json.load(file2)
with open('data_merge.json', 'w', encoding='utf8') as file:
    json.dump(data1 | data2, file)
# ----------------------------------------
import json
with open('people.json', encoding='utf8') as file:
    data = json.load(file)
    set_ = set()
    list_ = []
    for obj in data:
        for key in obj:
            set_.add(key)
    for obj in data:
        list_.append(dict.fromkeys(set_) | obj)
with open('updated_people.json', 'w', encoding='utf8') as file:
    json.dump(list_, file)


import json
with open('people.json', encoding='utf-8') as js:
    content = json.load(js)
keys = set()
for data in content:
    keys |= data.keys()
for data in content:
    data |= dict.fromkeys(keys - data.keys())
with open('updated_people.json', 'w') as js:
    json.dump(content, js, indent=3)
# ----------------------------------------
import json
with open('countries.json', encoding='utf8') as file:
    data = json.load(file)
    dict_ = {}
    for obj in data:
        dict_[obj['religion']] = dict_.get(obj['religion'], []) + [obj['country']]
with open('religion.json', 'w', encoding='utf8') as file:
    json.dump(dict_, file)
# ----------------------------------------
import csv
with (open('playgrounds.csv', encoding='utf-8') as file):
    rows = list(csv.reader(file, delimiter=';'))
    dict_ = {}
    for row in rows[1:]:
        dict_[row[1]] = dict_.get(row[1], {row[2]: []})

        dict_[row[1]][row[2]] = dict_[row[1]].get(row[2], []) + [row[3]]
#       dict_2 = dict_[row[1]]
#       dict_2[row[2]] = dict_2.get(row[2], []) + [row[3]]

import json
with open('addresses.json', 'w', encoding='utf8') as file:
    json.dump(dict_, file, ensure_ascii=False)
# ----------------------------------------
import json
import csv
with open('students.json', encoding='utf8') as file:
    data = json.load(file)
    list_ = []
    for obj in data:
        if int(obj['age']) >= 18 and int(obj['progress']) >= 75:
            list_.append((obj['name'], obj['phone']))
with open('data.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
    writer.writerow(['name', 'phone'])

    writer.writerows(sorted(list_))
#   for name, phone in sorted(list_):
#       writer.writerow([name, phone])
# ----------------------------------------
import json
import datetime as dt
with (open('pools.json', encoding='utf8') as file):
    data = json.load(file)
    dict_ = {'Length': 0, 'Width': 0, 'Address': ''}
    for obj in data:
        hours = obj['WorkingHoursSummer']['Понедельник'].split('-')
        if dt.datetime.strptime(hours[0], '%H:%M') <= dt.datetime(1900, 1, 1, 10) and dt.datetime.strptime(hours[1], '%H:%M') >= dt.datetime(1900, 1, 1, 12):
            if obj['DimensionsSummer']['Length'] > dict_['Length']:
                dict_['Length'] = obj['DimensionsSummer']['Length']
                dict_['Width'] = obj['DimensionsSummer']['Width']
                dict_['Address'] = obj['Address']
            if obj['DimensionsSummer']['Length'] == dict_['Length'] and obj['DimensionsSummer']['Width'] > dict_['Width']:
                dict_['Length'] = obj['DimensionsSummer']['Length']
                dict_['Width'] = obj['DimensionsSummer']['Width']
                dict_['Address'] = obj['Address']
print(f"{dict_['Length']}x{dict_['Width']}", dict_['Address'], sep='\n')
# ----------------------------------------
import json, csv
with open('exam_results.csv', encoding='utf-8') as file:
    head, *rows = list(csv.reader(file, delimiter=','))
list_sort = sorted(rows, key=lambda x: (x[4], -int(x[3].translate(str.maketrans(({'-': '', ':': '', ' ': ''}))))))
email_old = ''
list_ = []
for name, surname, score, date_and_time, email in list_sort:
    if email != email_old:
        dict_ = {'name': name, 'surname': surname, 'best_score': int(score), 'date_and_time': date_and_time, 'email': email}
        list_.append(dict_)
        email_old = email
with (open('best_scores.json', 'w',  encoding='utf8') as file):
    json.dump(list_, file)
# ----------------------------------------
import json
with open('food_services.json', encoding='utf8') as file:
    list_ = json.load(file)
dict_1, dict_2 = {}, {}
for obj in list_:
    dict_1[obj['District']] = dict_1.get(obj['District'], 0) + 1
    if obj['OperatingCompany']:
        dict_2[obj['OperatingCompany']] = dict_2.get(obj['OperatingCompany'], 0) + 1
print(*max(dict_1.items(), key=lambda x: x[1]), sep=': ')
print(*max(dict_2.items(), key=lambda x: x[1]), sep=': ')
# ----------------------------------------
import json
with open('food_services.json', encoding='utf8') as file:
    list_ = json.load(file)
dict_ = {}
for obj in list_:
    dict_[obj['TypeObject']] = dict_.get(obj['TypeObject'], []) + [(obj['Name'], obj['SeatsCount'])]
for k, v in sorted(dict_.items()):
    m = max(v, key=lambda x: x[1])
    print(f'{k}: {m[0]}, {m[1]}')


import json
data = {}
with open("food_services.json", encoding="utf-8") as sourse:
    data_json = json.load(sourse)
for elem in data_json:
    if data.get(elem["TypeObject"], (0, 0))[-1] < elem["SeatsCount"]:
        data[elem["TypeObject"]] = elem["Name"], elem["SeatsCount"]
[print(f"{k}: {v[0]}, {v[1]}") for k, v in sorted(data.items())]
# ======================================== 4.5
from zipfile import ZipFile
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
print(sum(not el.is_dir() for el in info))
# ----------------------------------------
from zipfile import ZipFile
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
print(f'Объем исходных файлов: {sum(f.file_size for f in info)} байт(а)')
print(f'Объем сжатых файлов: {sum(f.compress_size for f in info)} байт(а)')
# ----------------------------------------
from zipfile import ZipFile
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
t = min((f.compress_size / f.file_size * 100, f.filename) for f in info if not f.is_dir())
print(t[1].rsplit('/', 1)[1])
# ----------------------------------------
from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
t = (f.filename.split('/')[-1] for f in info if not f.is_dir() and datetime(*f.date_time) > datetime(2021, 11, 30, 14, 22, 0))
print(*sorted(t), sep='\n')
# ----------------------------------------
from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as zip_file:
    info = sorted(zip_file.infolist(), key=lambda x: x.filename.split('/')[-1])
    for file in info:
        if not file.is_dir():
            print(file.filename.split('/')[-1])
            print(f'  Дата модификации файла: {datetime(*file.date_time)}')
            print(f'  Объем исходного файла: {file.file_size} байт(а)')
            print(f'  Объем сжатого файла: {file.compress_size} байт(а)')
            print()
# ----------------------------------------
from zipfile import ZipFile
file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
with ZipFile('files.zip', mode='w') as zip_file:
    [zip_file.write(file) for file in file_names]
# ----------------------------------------
from zipfile import ZipFile
import os.path
file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']
with ZipFile('files.zip', mode='w') as zip_file:
    [zip_file.write(file) for file in file_names if os.path.getsize(file) <= 100]


with ZipFile('files.zip', mode='w') as zip_file:
    for file_name in file_names:
        with open(file_name, 'rb') as bite_file:
            size = len(bite_file.read())
        if size < 100:
            zip_file.write(file_name, file_name)
# ----------------------------------------
from zipfile import ZipFile
def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            for arg in args:
                zip_file.extract(arg)
        else:
            zip_file.extractall()


from zipfile import ZipFile
def extract_this(zip_name: str, *args):
    with ZipFile(zip_name) as zip_file:
        zip_file.extractall(members=args or None)
# ----------------------------------------
from zipfile import ZipFile
import json
players = []
with ZipFile('data.zip') as zip_file:
    list_ = [f for f in zip_file.namelist() if f.endswith('.json')]
    for json_file in list_:
        zip_file.extract(json_file)
        with open(json_file, encoding='utf-8') as file:
            try:
                data = json.load(file)
            except:
                continue
            if data.get('team', '') == 'Arsenal':
                players.append((data.get('first_name', ''), data.get('last_name', '')))
for first_name, last_name in sorted(players):
    print(first_name, last_name)


from zipfile import ZipFile
import json
def is_correct_json(string):
    try:
        return bool(json.loads(string))
    except:
        return False
players = []
with ZipFile('data.zip') as zip_file:
    list_ = [f for f in zip_file.namelist() if f.endswith('.json')]
    for json_file in list_:
        with zip_file.open(json_file) as file:
            file_decoded = file.read().decode('utf-8', 'ignore')
            if is_correct_json(file_decoded):
                data = json.loads(file_decoded)
                if data.get('team', '') == 'Arsenal':
                    players.append((data.get('first_name', ''), data.get('last_name', '')))
for first_name, last_name in sorted(players):
    print(first_name, last_name)
# ----------------------------------------
from zipfile import ZipFile
import math
def max_size(size):
    """Принимает число в байтах и возвращает число в B, KB, MB, GB"""
    if not size:
        return ''
    unit_names = ('B', 'KB', 'MB', 'GB', 'TB')
    pwr = math.floor(math.log(size, 1024))
    return round(size / 1024 ** pwr), unit_names[pwr]
with ZipFile('desktop.zip') as zip_file:
    for el in zip_file.infolist():
        info = (el.filename.strip('/').split('/'))
        print('  ' * (len(info) - 1) + info[-1], *max_size(el.file_size))
# ======================================== 4.6
import pickle
dogs = {'Ozzy': 2, 'Filou': 7, 'Luna': 4, 'Skippy': 11, 'Barco': 13, 'Balou': 10, 'Laika': 15}
with open('dogs.pkl', mode='wb') as file:
    pickle.dump(dogs, file)
# ----------------------------------------
import pickle
import sys
filename, *args = [line.strip() for line in sys.stdin]
with open(filename, 'rb') as file:
    obj = pickle.load(file)
print(obj(*args))
# ----------------------------------------
import pickle
def filter_dump(filename, objects, typename):
    objects_new = [obj for obj in objects if type(obj) == typename]
    with open(filename, 'wb') as file:
        pickle.dump(objects_new, file)
# ----------------------------------------
import pickle
filename, c_sum = input(), int(input())
with open(filename, 'rb') as file:
    obj = pickle.load(file)
    list_ = list(filter(lambda x: isinstance(x, int), obj))
    if not list_:
        c_sum_real = 0
    elif isinstance(obj, list):
        c_sum_real = min(list_) * max(list_)
    elif isinstance(obj, dict):
        c_sum_real = sum(list_)
    print('Контрольные суммы совпадают' if c_sum_real == c_sum else 'Контрольные суммы не совпадают')


import pickle
name, sm = input(), int(input())
with open(name, 'rb') as f:
    obj = pickle.load(f)
    lst = [i for i in obj if type(i) == int] or [0]
    check = sum(lst) if type(obj) == dict else max(lst)*min(lst)
    print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][sm == check])
# ======================================== 6.2
import string
in1 = input()
in2 = input().lower()
dict_ = dict(zip(string.ascii_lowercase, in1))
print(in2.translate(in2.maketrans(dict_)))


from string import ascii_lowercase
translator = str.maketrans(ascii_lowercase, input())
print(input().lower().translate(translator))
# ======================================== 6.4
from collections import namedtuple
Fruit = namedtuple('Fruit', ['name', 'color', 'vitamins'])
# ----------------------------------------
from collections import namedtuple
Game = namedtuple('Game', 'name developer publisher')
ExtendedGame = namedtuple('ExtendedGame', [*Game._fields, 'release_date', 'price'])
# ----------------------------------------
import pickle
from collections import namedtuple
Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])
with open('data.pkl', mode='rb') as file:
    for animal in pickle.load(file):
        for field, value in zip(Animal._fields, animal):
            print(f'{field}: {value}')
        print()
# ----------------------------------------
from collections import namedtuple
User = namedtuple('User', ['name', 'surname', 'email', 'plan'])
users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]
subscription = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 'Basic': 4}
for user in sorted(users, key=lambda x: (subscription[x.plan], x.email)):
    print(f'{user.name} {user.surname}')
    print(f'  Email: {user.email}')
    print(f'  Plan: {user.plan}')
    print()
# ----------------------------------------
import csv
from collections import namedtuple
from datetime import datetime
with open('meetings.csv', encoding='utf-8') as file:
    head, *rows = list(csv.reader(file, delimiter=','))
Friend = namedtuple('Friend', [*head[:2], 'meeting_datetime'])
friends = []
for friend in rows:
    friends.append(Friend(*(friend[0], friend[1], datetime.strptime(f'{friend[2]} {friend[3]}', '%d.%m.%Y %H:%M'))))
for friend in sorted(friends, key=lambda x: x.meeting_datetime):
    print(friend.surname, friend.name)
# ======================================== 6.5
from collections import defaultdict
data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]
ddict_ = defaultdict(int)
for name, amount in data:
    ddict_[name] += amount
for key, value in sorted(ddict_.items()):
    print(f'{key}: ${value}')
# ----------------------------------------
from collections import defaultdict
staff = [('Sales', 'Robert Barnes'), ('Developing', 'Thomas Porter'), ('Accounting', 'James Wilkins'), ('Sales', 'Connie Reid'), ('Accounting', 'Brenda Davis'), ('Developing', 'Miguel Norris'), ('Accounting', 'Linda Hudson'), ('Developing', 'Deborah George'), ('Developing', 'Nicole Watts'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Bernice Ramos'), ('Sales', 'Jose Taylor'), ('Sales', 'Katie Warner'), ('Accounting', 'Steven Diaz'), ('Accounting', 'Kimberly Reynolds'), ('Accounting', 'John Watts'), ('Accounting', 'Dale Houston'), ('Developing', 'Arlene Gibson'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Rosemary Garcia'), ('Marketing', 'Ralph Morgan'), ('Marketing', 'Sam Davis'), ('Marketing', 'Gail Hill'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Casey Jenkins'), ('Sales', 'Evelyn Martin'), ('Accounting', 'Aaron Ferguson'), ('Marketing', 'Andrew Clark'), ('Marketing', 'John Gonzalez'), ('Developing', 'Wilma Woods'), ('Sales', 'Marie Cooper'), ('Accounting', 'Kay Scott'), ('Sales', 'Gladys Taylor'), ('Accounting', 'Ann Bell'), ('Accounting', 'Craig Wood'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Mario Reynolds'), ('Marketing', 'Helen Taylor'), ('Marketing', 'Mary King'), ('Accounting', 'Jane Jackson'), ('Marketing', 'Carol Peters'), ('Sales', 'Alicia Mendoza'), ('Accounting', 'Edna Cunningham'), ('Developing', 'Joyce Rivera'), ('Sales', 'Joseph Lee'), ('Sales', 'John White'), ('Marketing', 'Charles Bailey'), ('Sales', 'Chester Fernandez'), ('Sales', 'John Washington')]
ddict_ = defaultdict(int)
for name, _ in staff:
    ddict_[name] += 1
for key, value in sorted(ddict_.items()):
    print(f'{key}: {value}')
# ----------------------------------------
from collections import defaultdict
staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'), ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'), ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'), ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'), ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'), ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'), ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'), ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'), ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'), ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'), ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'), ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'), ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'), ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'), ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'), ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'), ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'), ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'), ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'), ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'), ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'), ('Accounting', 'Dale Houston')]
ddict_ = defaultdict(list)
for key, value in staff_broken:
    ddict_[key] += [value]
for key, value in sorted(ddict_.items()):
    print(f'{key}: ', end='')
    print(*sorted(set(value)), sep=', ')
# ----------------------------------------
from collections import defaultdict
def wins(list_):
    ddict_ = defaultdict(set)
    for key, value in list_:
        ddict_[key].add(value)
      # ddict_[key] |= {value}  # 60% longer
    return ddict_
# result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])
# for winner, losers in sorted(result.items()):
#     print(winner, '->', *sorted(losers))
# ----------------------------------------
from collections import defaultdict
def flip_dict(dict_):
    ddict_ = defaultdict(list)
    for key, values in dict_.items():
        for value in values:
            ddict_[value].append(key)
          # ddict_[value] += [key]  # 60% longer
    return ddict_
# data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}
# print(flip_dict(data))
# ----------------------------------------
from collections import defaultdict
def best_sender(messages, senders):
    ddict_ = defaultdict(int)
    for key, value in zip(senders, messages):
        ddict_[key] += len(value.split())
    return sorted(ddict_, key=lambda x: (ddict_[x], x), reverse=True)[0]
  # return max(ddict_, key=lambda x: (ddict_[x], x))
# messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
# senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
# print(best_sender(messages, senders))
# ======================================== 6.6
from collections import OrderedDict
data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
for key in list(data):
    data.move_to_end(key, last=False)
print(data)


from collections import OrderedDict
data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
print(OrderedDict(reversed(data.items())))
# ----------------------------------------
from collections import OrderedDict
data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
data_new = OrderedDict()
rule = False
while data:
    key, value = data.popitem(last=rule)
    data_new[key] = value
    rule = not rule
print(data_new)
# ----------------------------------------
from collections import OrderedDict
def custom_sort(ordered_dict, by_values=False):
    for key in sorted(ordered_dict, key=lambda x: ordered_dict[x] if by_values else x):
        ordered_dict.move_to_end(key)
# ======================================== 6.7
from collections import Counter
files = ['emoji_smile.jpeg', 'city-of-the-sun.mp3', 'dhook_hw.json', 'sample.xml',
         'teamspeak3.exe', 'project_module3.py', 'math_lesson3.mp4', 'old_memories.mp4',
         'spiritfarer.exe', 'backups.json', 'python_for_beg1.mp4', 'emoji_angry.jpeg',
         'exam_results.csv', 'project_main.py', 'classes.csv', 'plants.xml',
         'cant-help-myself.mp3', 'microsoft_edge.exe', 'steam.exe', 'math_lesson4.mp4',
         'city.jpeg', 'bad-disease.mp3', 'beauty.jpeg', 'hollow_knight_silksong.exe',
         'whatsapp.exe', 'photoshop.exe', 'telegram.exe', 'yandex_browser.exe',
         'math_lesson7.mp4', 'students.csv', 'emojis.zip', '7z.zip',
         'bones.mp3', 'python3.zip', 'dhook_lsns.json', 'carl_backups.json',
         'forest.jpeg', 'python_for_pro8.mp4', 'yandexdisc.exe', 'but-you.mp3',
         'project_module1.py', 'nothing.xml', 'flowers.jpeg', 'grades.csv',
         'nvidia_gf.exe', 'small_txt.zip', 'project_module2.py', 'tab.csv',
         'note.xml', 'sony_vegas11.exe', 'friends.jpeg', 'data.pkl']
for key, value in sorted(Counter([i.split('.')[1] for i in files]).items()):
    print(f'{key}: {value}')
# ----------------------------------------
from collections import Counter
def count_occurences(word, words):
    word_counter = Counter(words.lower().split())
    return word_counter[word.lower()]
# ----------------------------------------
from collections import Counter
word_counter = Counter(input().lower().split(','))
for key, value in sorted(word_counter.items()):
    print(f'{key}: {value}')
# ----------------------------------------
from collections import Counter
word_counter = Counter(input().lower().split(','))
max_len = len(max(word_counter, key=len))
for key, value in sorted(word_counter.items()):
    sum_ = sum(ord(i) for i in key if i != ' ')
    print(f'{key.ljust(max_len)}: {sum_} UC x {value} = {sum_ * value} UC')


from collections import Counter
def get_price(product):
    return sum(map(ord, filter(str.isalpha, product)))
products = Counter(input().split(','))
pattern = '{}: {} UC x {} = {} UC'
spaces = max(map(len, products))
for product, count in sorted(products.items()):
    price = get_price(product)
    total = price * count
    product = product.ljust(spaces, ' ')
    print(pattern.format(product, price, count, total))
# ----------------------------------------
from collections import Counter
from string import ascii_lowercase
with open('pythonzen.txt', mode='r', encoding='UTF-8') as file:
    text = file.read()
letter_counter = Counter(text.lower())
for letter in ascii_lowercase:
    if letter_counter[letter]:
        print(f'{letter}: {letter_counter[letter]}')


from collections import Counter
with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    letters = Counter([letter for letter in file.read().lower() if letter.isalpha()])
for letter in sorted(letters):
    print(f'{letter}: {letters[letter]}')
# ======================================== 6.8
from collections import Counter
words = Counter(input().lower().split())
print(words.most_common(1)[0][0])
# ----------------------------------------
from collections import Counter
words = Counter(input().lower().split())
min_count = words.most_common()[-1][1]
print(*sorted([k for k, v in words.items() if v == min_count]), sep=', ')
# ----------------------------------------
from collections import Counter
words = Counter(input().lower().split())
max_count = words.most_common()[0][1]
print(max([k for k, v in words.items() if v == max_count]))
# ----------------------------------------
from collections import Counter
words = Counter(map(len, input().lower().split()))
for k, v in sorted(words.items(), key=lambda x: x[1]):
    print(f'Слов длины {k}: {v}')
# ----------------------------------------
import sys
from collections import Counter
c = Counter()
for data in sys.stdin:
    name, score = data.split()
    c.update({name: int(score)})
print(c.most_common()[-2][0])


from collections import Counter
c = Counter({i: int(j) for i, j in (s.split() for s in open(0))})
print(c.most_common()[-2][0])
# ----------------------------------------
from collections import Counter
data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
data.min_values = lambda: [(k, v) for k, v in data.items() if v == min(data.values())]
data.max_values = lambda: [(k, v) for k, v in data.items() if v == max(data.values())]
# ----------------------------------------
import csv
from collections import Counter
with open('name_log.csv', encoding='utf-8') as file:
    _, *reader = csv.reader(file)
    counter_ = Counter([email for _, email, _ in reader])
    print(*[f'{k}: {v}' for k, v in sorted(counter_.items())], sep='\n')
# ----------------------------------------
from collections import Counter
def scrabble(symbols, word):
    return Counter(word.lower()) <= Counter(symbols.lower())
# ----------------------------------------
from collections import Counter
def print_bar_chart(data, mark):
    max_len = max(map(len, data))
    for k, v in Counter(data).most_common():
        print(f'{k.ljust(max_len)} |{mark * v}')
# ----------------------------------------
import csv, json
from collections import Counter
counter_year = Counter()
files = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']
for file in files:
    with open(file, encoding='utf-8') as file:
        _, *reader = csv.reader(file)
        counter_year += Counter({product: sum(map(int, months)) for product, *months in reader})
with open('prices.json', encoding='utf8') as file:
    prices = json.load(file)
print(sum(prices[product] * amount for product, amount in counter_year.items()))
# ----------------------------------------
from collections import Counter
counter_ = Counter(map(int, input().split()))
sum_ = 0
for _ in range(int(input())):
    book, price = map(int, input().split())
    if counter_[book]:
        counter_ -= Counter({book: 1})
        sum_ += price
print(sum_)


from collections import Counter
books = Counter(map(int, input().split()))
total = 0
for _ in range(int(input())):
    book, price = map(int, input().split())
    total += bool(books[book]) * price
    books -= Counter({book: 1})
print(total)
# ======================================== 6.9
import json
from collections import ChainMap
with open('zoo.json', encoding='utf8') as file:
    animals = ChainMap(*json.load(file))
    print(sum(animals.values()))
# ----------------------------------------
from collections import ChainMap, Counter
bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}
price = ChainMap(bread, meat, sauce, vegetables, toppings)
burger = input().split(',')
total, max_len, max_ljust = 0, 0, 0
list_ = []
for ingr, amount in sorted(Counter(burger).items()):
    list_.append((ingr, amount))
    total += amount * price[ingr]
    max_len = max(max_len, len(ingr) + len(str(amount)) + 3)
    max_ljust = max(max_ljust, len(ingr))
max_len = max(max_len, len(str(total)) + 7)
for el in list_:
    print(f'{el[0].ljust(max_ljust)} x {el[1]}')
print('-' * max_len)
print(f'ИТОГ: {total}р')
# ======================================== 6.10
from collections import ChainMap
def get_all_values(chainmap, key):
    return {cm[key] for cm in chainmap.maps if key in cm}
# ----------------------------------------
from collections import ChainMap, Counter
def deep_update(chainmap, key, value):
    try:
        chainmap[key]
        for cm in chainmap.maps:
            if key in cm:
                cm[key] = value
    except KeyError:
        chainmap[key] = value


from collections import ChainMap
def deep_update(chainmap, key, value):
    if key in chainmap:
        [cm.update({key: value}) for cm in chainmap.maps if key in cm]
    else:
        chainmap[key] = value
# ----------------------------------------
from collections import ChainMap
def get_value(chainmap, key, from_left=True):
    if key not in chainmap:
        return None
    if from_left:
        chainmap.maps.reverse()
    return [cm[key] for cm in chainmap.maps if key in cm][-1]


from collections import ChainMap
def get_value(chainmap, key, from_left=True):
    for item in chainmap.maps if from_left else reversed(chainmap.maps):
        if key in item:
            return item[key]
    return None


# side effect !!!
from collections import ChainMap
def get_value(chainmap, key, from_left=True):
    if not from_left:
        chainmap.maps.reverse()
    return chainmap.get(key)
# ======================================== 7.1
total = 0
with open('data.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        total = total + 1
print(total)
# ----------------------------------------
def swapcase_vowels(string):
    vowels = 'aeiouy'
    swapped_string = ''
    for char in string:
        if char in vowels:
            char = char.upper()
        swapped_string += char
    return swapped_string
# ----------------------------------------
a = int(input())
b = int(input())
numbers = []
for i in range(a, b+1):
    if i % 7 == 0:
        numbers.append(i)
print(numbers)
# ----------------------------------------
def get_max_index(numbers):
    max_index = 0
    max_value = numbers[0]
    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
            max_index = index
    return max_index
# ======================================== 7.2
blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
              {'Likes': 13, 'Comments': 2, 'Shares': 1},
              {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
              {'Comments': 4, 'Shares': 2},
              {'Photos': 8, 'Comments': 1, 'Shares': 1},
              {'Photos': 3, 'Likes': 19, 'Comments': 3}]
total_likes = 0
for post in blog_posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        total_likes -= 1
print(total_likes)
# ----------------------------------------
food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
fifth = []
for x in food:
    try:
        fifth.append(x[4])
    except IndexError:
        fifth.append('_')
print(fifth)
# ----------------------------------------
numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
remainders = []
for number in numbers:
    try:
        remainders.append(36 % number)
    except ZeroDivisionError:
        pass
print(remainders)
# ----------------------------------------
import sys
sum_, counter = 0, 0
for line in sys.stdin:
    try:
        sum_ += int(line)
    except ValueError:
        try:
            sum_ += float(line)
        except:
            counter += 1
print(sum_)
print(counter)
# ======================================== 7.3
from calendar import month_name
class InvalidRangeException(Exception):
    """Введено число из недопустимого диапазона [1:12]"""
    pass
try:
    month = int(input())
    if not 1 <= month <= 12:
        raise InvalidRangeException
    print(month_name[month])
except InvalidRangeException:
    print('Введено число из недопустимого диапазона')
except:
    print('Введено некорректное значение')


from calendar import month_name
try:
    print(dict(enumerate(month_name[1:], 1))[int(input())])
except KeyError:
    print('Введено число из недопустимого диапазона')
except:
    print('Введено некорректное значение')
# ----------------------------------------
def add_to_list_in_dict(data, key, element):
    try:
        data[key].append(element)
    except KeyError:
        data[key] = [element]
# ----------------------------------------
try:
    with open(input(), encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('Файл не найден')
# ======================================== 7.4
def get_weekday(number):
    week = ['', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if not 1 <= number <= 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    return week[number]
# ----------------------------------------
def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    return len(names) + 1
# ----------------------------------------
import json
try:
    with open(input(), encoding='utf8') as file:
        print(json.load(file))
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')


import json
try:
    with open(input(), encoding='utf-8') as f:
        print(json.load(f))
except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    print('Ошибка при десериализации')
# ======================================== 7.5
def is_good_password(string):
    return all([len(string) >= 9,
                any(c.islower() for c in string),
                any(c.isupper() for c in string),
                any(c.isdigit() for c in string)])
# ----------------------------------------
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if not any(c.islower() for c in string) or not any(c.isupper() for c in string):
        raise LetterError
    if not any(c.isdigit() for c in string):
        raise DigitError
    return True
# ----------------------------------------
import sys

class PasswordError(Exception):
    pass
class LengthError(PasswordError):
    pass
class LetterError(PasswordError):
    pass
class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError('LengthError')
    if not any(c.islower() for c in string) or not any(c.isupper() for c in string):
        raise LetterError('LetterError')
    if not any(c.isdigit() for c in string):
        raise DigitError('DigitError')
    return True

for line in sys.stdin.readlines():
    try:
        if is_good_password(line.strip()):
            print('Success!')
            break
    except Exception as err:
        print(err)
# ======================================== 8.2
def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)
# ----------------------------------------
def func(start, stop):
    if start <= stop:
        print(start)
        func(start + 1, stop)
func(1, 100)
# ----------------------------------------
numbers = [243, -279, 395, 130, 89, 269, 861, 669, 939, 367, -46, 710, 841, -280, -244, 274, -132, 273, 418, 432, -341, 437, 360, 960, 195, 792, 106, 461, -35, 980, -80, 540, -358, 69, -26, -416, 597, 96, 533, 232, 755, 894, 331, 323, -383, -386, 231, 436, 553, 967, 166, -151, 772, 434, 325, 301, 275, 431, 556, 728, 558, 702, 463, 127, 984, 212, 876, -287, -16, -177, 577, 604, 116, 500, 653, 669, 916, 802, 817, 762, -210, -353, 144, -351, 777, 805, 692, 22, -303, 249, 190, 411, 236, -274, 174, 380, 71, 124, -85, 430]
def func(numbers):
    def rec(index):
        if index < len(numbers):
            print(f'Элемент {index}: {numbers[index]}')
            rec(index + 1)
    rec(0)
func(numbers)
# ----------------------------------------
def func():
    n = int(input())
    if n != 0:
        func()
    print(n)
func()
# ----------------------------------------
def triangle(h):
    def rec(h, stop=0):
        if h > stop:
            print('*' * h)
            rec(h - 1)
    rec(h)


def triangle(h):
    if h:
        print('*' * h)
        triangle(h - 1)
# ----------------------------------------
def triangle(h):
    def rec(step=1):
        if step <= h:
            print('*' * step)
            rec(step + 1)
    rec()


def triangle(h):
    if h > 0:
        triangle(h - 1)
        print('*' * h)
# ----------------------------------------
def clock():
    def rec(index=1, str_len=16, step=4):
        if index < 4:
            print(f'{str(index) * str_len}'.center(16))
            rec(index + 1, str_len - step)
        print(f'{str(index) * str_len}'.center(16))
    rec()
clock()
# ----------------------------------------
def print_digits(number):
    if number:
        print(number % 10)
        print_digits(number // 10)
# ----------------------------------------
def print_digits(number):
    if number:
        print_digits(number // 10)
        print(number % 10)
# ======================================== 8.3
def func(number):
    if number == number % 10:
        return 1
    else:
        return 1 + func(number // 10)
print(func(int(input())))
# ----------------------------------------
def func(number):
    if number < 10:
        return number
    return number % 10 + func(number // 10)
print(func(int(input())))
# ----------------------------------------
def number_of_frogs(year):
    if year == 1:
        return 77
    return 3 * (number_of_frogs(year - 1) - 30)
# ----------------------------------------
def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    return numbers[start] + range_sum(numbers, start + 1, end)
# ----------------------------------------
def get_pow(a, n):
    if n == 0:
        return 1
    return a * get_pow(a, n - 1)
# ----------------------------------------
def get_fast_pow(a, n):
    if n == 0:
        return 1
    if not n % 2:
        return get_fast_pow(a * a, n // 2)
    else:
        return a * get_fast_pow(a, n - 1)
# ----------------------------------------
def recursive_sum(a, b):
    if a + b == 0:
        return 0
    return 1 + recursive_sum(a, b - 1)


def recursive_sum(a, b):
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)
# ----------------------------------------
def is_power(number):
    if number == 1:
        return True
    elif number % 2 == 0:
        return is_power(number // 2)
    else:
        return False
# ----------------------------------------
def tribonacci(n):
    cache = {1: 1, 2: 1, 3:1}
    def trib_rec(n):
        result = cache.get(n)
        if result is None:
            result = trib_rec(n - 3) + trib_rec(n - 2) + trib_rec(n - 1)
            cache[n] = result
        return result
    return trib_rec(n)
# ----------------------------------------
def is_palindrome(string):
    def rec(index=0):
        if string == '':
            return True
        elif index <= len(string) // 2:
            return string[index] == string[-index - 1] and rec(index + 1)
        return True
    return rec()


def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])
# ----------------------------------------
def to_binary(number):
    if number < 2:
        return str(number)
    return to_binary(number // 2) + str(number % 2)
# ----------------------------------------
def func(n):
    print(n)
    if n > 0:
        func(n - 5)
        print(n)
func(int(input()))
# ======================================== 8.4
def recursive_sum(nested_lists):
    if not nested_lists:
        return 0
    elif isinstance(nested_lists, int):
        return nested_lists
    else:
        return sum([recursive_sum(i) for i in nested_lists])


def recursive_sum(nested_lists):
    total = 0
    for elem in nested_lists:
        if isinstance(elem, list):
            total += recursive_sum(elem)
        else:
            total += elem
    return total
# ----------------------------------------
def linear(nested_lists):
    list_ = []
    def linear_rec(nested_lists):
        if isinstance(nested_lists, int):
            list_.append(nested_lists)
        else:
            for i in nested_lists:
                linear_rec(i)
        return list_
    return linear_rec(nested_lists)


def linear(nested_lists):
    list_ = []
    for elem in nested_lists:
        if isinstance(elem, list):
            list_.extend(linear(elem))
        else:
            list_.append(elem)
    return list_
# ----------------------------------------
def get_value(data, key):
    if key in data:
        return data[key]
    for v in data.values():
        if type(v) == dict:
            value = get_value(v, key)
            if value is not None:
                return value
# ----------------------------------------
def get_all_values(data, key):
    set_ = set()
    if key in data:
        set_.add(data[key])
    for v in data.values():
        if isinstance(v, dict):
            set_ = set_.union(get_all_values(v, key))  # set_ |= get_all_values(v, key)
    return set_
# ----------------------------------------
def dict_travel(data):
    dict_ = {}
    def rec(data=data, sub=''):
        for key, value in data.items():
            if isinstance(value, dict):
                rec(value, sub=f'{sub}{key}.')
            else:
                dict_[f'{sub}{key}'] = value
        return dict_
    print(*[f'{key}: {value}' for key, value in sorted(rec().items())], sep='\n')


def dict_travel(data, parent_key=''):
    for key, value in sorted(data.items()):
        key = f'{parent_key}.{key}' if parent_key else key
        if isinstance(value, dict):
            dict_travel(value, key)
        else:
            print(f'{key}: {value}')
# ======================================== 9.1
for i in range(ord('a'), ord('z') + 1):
    print(chr(i))
# ----------------------------------------
def convert(number):
    return (bin(number).replace('0b', ''), oct(number).replace('0o', ''), hex(number).replace('0x', '').upper())


def convert(number):
    return f'{number:b}', f'{number:o}', f'{number:X}'
# ----------------------------------------
films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6},
         'Encanto': {'imdb': 7.3, 'kinopoisk': 7.4},
         'The Witcher': {'imdb': 8.2, 'kinopoisk': 7.3},
         'Ghostbusters: Afterlife': {'imdb': 7.3, 'kinopoisk': 8},
         'Harry Potter 20th Anniversary: Return to Hogwarts': {'imdb': 8.1, 'kinopoisk': 8.2},
         'Shingeki no Kyojin': {'imdb': 9.0, 'kinopoisk': 8.3},
         'The Matrix': {'imdb': 8.7, 'kinopoisk': 8.5},
         'The Dark Knight': {'imdb': 9.0, 'kinopoisk': 8.5},
         'The Shawshank Redemption': {'imdb': 9.3, 'kinopoisk': 9.1},
         'Avengers: Endgame': {'imdb': 8.4, 'kinopoisk': 7.7}}
print(min(films, key=lambda x: sum(films[x].values())))
# ----------------------------------------
def non_negative_even(numbers):
    return all(not i % 2 and i >= 0 for i in numbers)
# ----------------------------------------
def is_greater(lists, numbers):
    return any(sum(l) > numbers for l in lists)
# ----------------------------------------
def custom_isinstance(objects, typeinfo):
    return sum(isinstance(o, typeinfo) for o in objects)
# ----------------------------------------
numbers = [-7724, 5023, 3197, -102, -4129, -880, 5857, -2866, -8913, 1195, 9809, 5347, -8071, 903, 3030, -4347, -3354, 1024, 8670, 4210, -5228, 8900, 4823, -2002, 4900, 9520, -3658, 1104, -9554, 3064, 9632, -8701, 3384, 4370, 2034, 7822, -9694, 3347, 7440, -8459, 3238, -5193, -3381, 5281, 9022, 5559, 7593, -6540, -6204, -2483, 8729, 5810, -8254, -9846, -1801, 4882, 3838, -3140, 7609, -3325, 6026, 2994, -1677, 1266, -1893, -4408, -5722, -2841, 9812, 5837, -7474, 4624, -664, 6998, 7888, -971, 8810, 3812, -5396, 2593, 512, -4634, 9735, -3062, 9031, -9300, 3657, 6332, 7552, 8125, -725, 4392, 1727, 8194, -2828, -4314, -8967, -7912, -1363, -5957]
print(max(enumerate(numbers), key=lambda x: x[1])[0])
# ----------------------------------------
def my_pow(number):
    return sum(int(n)**power for power, n in enumerate(str(number), 1))
# ----------------------------------------
names = ['Moana', 'Cars', 'Zootopia', 'Ratatouille', 'Coco', 'Inside Out', 'Finding Nemo', 'Frozen']
budgets = [150000000, 120000000, 150000000, 150000000, 180000000, 175000000, 94000000, 150000000]
box_offices = [643331111, 462216280, 1023784195, 620702951, 807082196, 857611174, 940335536, 1280802282]
for n, b, bo in sorted(zip(names, budgets, box_offices)):
        print(f'{n}: {bo - b}$')
# ----------------------------------------
import itertools
def zip_longest(*args, fill=None):
    return list(itertools.zip_longest(*args, fillvalue=fill))
# ----------------------------------------
str_ = input()
print(''.join(sorted(filter(lambda x: x.islower(), str_))) +
      ''.join(sorted(filter(lambda x: x.isupper(), str_))) +
      ''.join(sorted(filter(lambda x: x.isdigit() and x in '13579', str_))) +
      ''.join(sorted(filter(lambda x: x.isdigit() and x in '02468', str_))))


from string import ascii_lowercase, ascii_uppercase
sort_list = list(ascii_lowercase) + list(ascii_uppercase) + list('1357902468')
print(''.join(sorted(input(), key=sort_list.index)))
# print(''.join(sorted(input(), key=lambda x: sort_list.index(x))))


print(''.join(sorted(input(), key=lambda x: (x in '24680', x.isdigit(), x.isupper(), x))))
# ======================================== 9.2
def hash_as_key(objects):
    dict_ = {}
    for i in objects:
        if hash(i) not in dict_:
            dict_[hash(i)] = i
        elif isinstance(dict_[hash(i)], list):
            dict_[hash(i)].append(i)
        else:
            dict_[hash(i)] = [dict_[hash(i)], i]
    return dict_
# ----------------------------------------
data = eval(input())
if isinstance(data, list):
    print(data[-1])
elif isinstance(data, tuple):
    print(data[0])
else:
    print(len(data))


n = eval(input())
print(eval({list: 'n[-1]', tuple: 'n[0]', set: 'len(n)'}[type(n)]))
# ----------------------------------------
import sys
print(max([eval(line.strip()) for line in sys.stdin]))


import sys
print(max(map(eval, sys.stdin)))
# ----------------------------------------
func_ = input()
start, end = map(int, input().split())
list_ = [eval(func_) for x in range(start, end + 1)]
print(f'Минимальное значение функции {func_} на отрезке [{start}; {end}] равно {min(list_)}')
print(f'Максимальное значение функции {func_} на отрезке [{start}; {end}] равно {max(list_)}')
# func_ = input()
# exec(f'def func(x): return {func_}')
# ======================================== 9.3
data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733, 'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288, None, -708.3036176571618]
print(*map(int, filter(lambda x: isinstance(x, (int, float)), data)), sep='\n')
# ----------------------------------------
numbers = [4754, -4895, -364, -4764, 4683, 1639, -43, 228, -2701, -1503, 1223, 4340, -1296, 3939, -345, 623, -3275, 1003, 4367, -1739, 550, -1217, -1334, 1526, -4359, -3028, -4663, 3356, 3887, 4297, -1982, 1013, 3299, 3556, -3324, 417, 3531, -3134, 1782, 4439, 1652, -985, 4327, 1517, 1225, -915, 2808, -3851, -1005, 3396, 2842, -3879, -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588, -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354, 4926, -352, -1187, -3313, 2741, 4786, -2689, 741, 4558, 1442, 62, -1099, -2201, -16, -3115, 1862, 2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148, 4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]
print(*map(lambda x: x**2, filter(lambda x: len(str(x)) == 2 and x % 9 == 0, map(abs, numbers))), sep='\n')
# ----------------------------------------
names = ['ульяна', 'арина', 'Дмитрий', 'Сергей', 'Яна', 'мила', 'Ольга', 'софья', 'семён', 'Никита', 'маргарита', 'Василиса', 'Кирилл', 'александр', 'александра', 'Иван', 'андрей', 'Родион', 'максим', 'алиса', 'Артём', 'софия', 'владимир', 'дамир', 'Валерий', 'степан', 'Алексей', 'Марк', 'олег', 'ирина', 'Милана', 'мия', 'денис', 'Фёдор', 'Елизавета', 'айлин', 'Варвара', 'валерия', 'Алёна', 'Николь', 'юлия', 'Ксения', 'пётр', 'георгий', 'Мария', 'глеб', 'илья', 'Захар', 'Дарья', 'Евгения', 'матвей', 'Серафим', 'екатерина', 'Тимофей', 'виктор', 'Егор', 'Ника', 'анна', 'даниил', 'тихон', 'вера', 'кира', 'Эмилия', 'Виктория', 'Игорь', 'полина', 'алина', 'Давид', 'анастасия', 'Вероника', 'ярослав', 'Руслан', 'татьяна', 'Демид', 'амелия', 'Элина', 'Арсен', 'евгений', 'мадина', 'дарина', 'Савелий', 'Платон', 'Аделина', 'диана', 'Айша', 'павел', 'Стефания', 'Тимур', 'Ева', 'Елисей', 'Артемий', 'григорий', 'Мирон', 'Мирослава', 'Мира', 'Марат', 'Лилия', 'роман', 'владислав', 'Леонид']
print(*sorted(map(str.title, filter(lambda x: x[0].lower() in ('ам') and len(x) > 4, names))))
# ----------------------------------------
fib = lambda x: [1, 1][x - 1] if x < 3 else fib(x - 1) + fib(x - 2)
fib = lambda x:  if x < 3 else fib(x - 1) + fib(x - 2)


d = {1: 1, 2: 1}
fib = lambda x: d[x] if x in d else d.setdefault(x, fib(x - 1) + fib(x - 2))
# ----------------------------------------
def print_operation_table(operation, rows, cols):
    for i in range(1, rows + 1):
        print(*[operation(i, j) for j in range(1, cols + 1)])
# ----------------------------------------
def verification(login, password, success, failure):
    if not any(c.isalpha() and c.isascii() for c in password):
        return failure(login, 'в пароле нет ни одной буквы')
    if not any(c.isupper() and c.isascii() for c in password):
        return failure(login, 'в пароле нет ни одной заглавной буквы')
    if not any(c.islower() and c.isascii() for c in password):
        return failure(login, 'в пароле нет ни одной строчной буквы')
    if not any(c.isdigit() for c in password):
        return failure(login, 'в пароле нет ни одной цифры')
    return success(login)


from string import ascii_letters, ascii_lowercase, ascii_uppercase
def verification(login, password, success, failure):
    try:
        assert set(password) & set(ascii_letters), 'в пароле нет ни одной буквы'
        assert set(password) & set(ascii_uppercase), 'в пароле нет ни одной заглавной буквы'
        assert set(password) & set(ascii_lowercase), 'в пароле нет ни одной строчной буквы'
        assert set(password) & set('0123456789'), 'в пароле нет ни одной цифры'
    except AssertionError as e:
        failure(login, e)
    else:
        success(login)
# ======================================== 9.4
def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """

    return sum(filter(lambda x: isinstance(x, (int, float)), elems))
# ----------------------------------------
def func(*args, sep=' ', end='\n'):
    return print_origin(*map(lambda x: x.upper() if isinstance(x, str) else x, args), sep=sep.upper(), end=end.upper())
print_origin = print
print = func


from sys import stdout
def print(*s, sep=" ", end="\n"):
    result = sep.upper().join(map(lambda x: str(x).upper() if type(x) is str else str(x), s)) + end.upper()
    stdout.write(result)
# ----------------------------------------
def polynom(x):
    if 'values' not in polynom.__dict__:
        polynom.values = set()
    value = x**2 + 1
    polynom.values.add(value)
    return value


def polynom(x):
    polynom.__dict__.setdefault('values', set())
    value = x**2 + 1
    polynom.values.add(value)
    return value


def polynom(x: float):
    value = x**2 + 1
    polynom.values.add(value)
    return value
polynom.values = set()
# ----------------------------------------
def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    return ''.join(filter(lambda x: x not in marks, text))


def remove_marks(text, marks):
    remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1
#   remove_marks.count             = remove_marks.__dict__.get('count', 0) + 1
    return ''.join(filter(lambda x: x not in marks, text))
# ======================================== 9.5
def power(degree):
    def inner(x):
        return x**degree
    return inner


def power(degree):
    return lambda x: x ** degree
# ----------------------------------------
def generator_square_polynom(a, b, c):
    return lambda x: a*x**2 + b*x + c
# ----------------------------------------
def sourcetemplate(url):
    def inner(**kwargs):
        return url + ('?' + '&'.join([f'{k}={v}' for k, v in sorted(kwargs.items())]) if kwargs else '')
    return inner


def sourcetemplate(url):
    return lambda **kwargs: url + ('?' + '&'.join([f'{k}={v}' for k, v in sorted(kwargs.items())]) if kwargs else '')
# ----------------------------------------
from datetime import date
def date_formatter(country_code):
    def ru(date):
        return date.strftime('%d.%m.%Y')
    def us(date):
        return date.strftime('%m-%d-%Y')
    def ca(date):
        return date.strftime('%Y-%m-%d')
    def br(date):
        return date.strftime('%d/%m/%Y')
    def fr(date):
        return date.strftime('%d.%m.%Y')
    def pt(date):
        return date.strftime('%d-%m-%Y')
    dict_ = {'ru': ru, 'us': us, 'ca': ca, 'br': br, 'fr': fr, 'pt': pt}
    return dict_[country_code]


from datetime import date
def date_formatter(country_code):
    dict_ = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d', 'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
    return lambda x: x.strftime(dict_[country_code])
# ----------------------------------------
def sort_priority(values, group):
    values.sort(key=lambda x: (x not in group, x in group, x))

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
(False, True, 2)
(False, True, 3)
(False, True, 5)
(False, True, 7)
(True, False, 1)
(True, False, 4)
(True, False, 6)
(True, False, 8)
# ======================================== 9.6
def get_digits(number: int | float) -> list[int]:
    return list(map(int, str(number).replace('.', '')))


def get_digits(number: int | float) -> list[int]:
    return [int(i) for i in str(number) if i.isdigit()]
# ----------------------------------------
def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    return {'name': grades['name'], 'top_grade': max(grades['grades'])}
# ----------------------------------------
def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step %= len(numbers)
    numbers[step:], numbers[:step] = numbers[:-step], numbers[-step:]


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step %= len(numbers)
    numbers[:] = numbers[-step:] + numbers[:-step]
# ----------------------------------------
def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {e: m for e, m in enumerate(matrix, 1)}


def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return dict(enumerate(matrix, 1))
# ======================================== 9.7
def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        res = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return res
    return wrapper
# ----------------------------------------
def new_print(func):
    def wrapper(*args, **kwargs):
        kwargs['sep'] = kwargs.get('sep', ' ').upper()
        kwargs['end'] = kwargs.get('end', '\n').upper()
        func(*map(lambda x: str(x).upper(), args), **kwargs)  # return None (in this case)
#       return func(*map(lambda x: str(x).upper(), args), **kwargs)
    return wrapper
print = new_print(print)
# ----------------------------------------
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper
# ----------------------------------------
def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*reversed(args), **kwargs)
    return wrapper
# ----------------------------------------
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res, 'Функция выполнилась без ошибок'
#           return f"({res.__repr__()}, 'Функция выполнилась без ошибок')"
        except:
            return None, 'При вызове функции произошла ошибка'
#           return f"({None}, 'При вызове функции произошла ошибка')"
    return wrapper


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            msg = 'Функция выполнилась без ошибок'
        except:
            res = None
            msg = 'При вызове функции произошла ошибка'
        finally:  # выполняется в любом случае
            return res, msg
    return wrapper
# ----------------------------------------
def takes_positive(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
#       all_args = [*args, *kwargs.values()]
        if not all(map(lambda x: isinstance(x, int), all_args)):
            raise TypeError
        if any(map(lambda x: x <= 0, all_args)):
            raise ValueError
        return func(*args, **kwargs)
    return wrapper
# ======================================== 9.8
# Шаблон декоратора общего назначения
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Что-то выполняется до вызова декорируемой функции
        value = func(*args, **kwargs)
        # декорируется возвращаемое значение функции
        # или что-то выполняется после вызова декорируемой функции
        return value
    return wrapper
# ----------------------------------------
import functools
def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        return value**2
    return wrapper
# ----------------------------------------
import functools
def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if not isinstance(value, str):
            raise TypeError
        return value    
    return wrapper
# ----------------------------------------
import functools
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        value = func(*args, **kwargs)
        print(f'TRACE: возвращаемое значение {func.__name__}(): {value.__repr__()}')
        return value
    return wrapper
# ----------------------------------------
@repeat(3)
@debug(True)
def beegeek():
    return 'beegeek'


beegeek = debug(True)(beegeek)
beegeek = repeat(3)(beegeek)


beegeek = repeat(3)(debug(True)(beegeek))
# ----------------------------------------
import functools
def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return value + string if to_the_end else string + value
#           return (string + value, value + string)[to_the_end]
        return wrapper
    return decorator


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'
print(get_bonus())
# ----------------------------------------
import functools
def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = f'<{tag}>' + func(*args, **kwargs) + f'</{tag}>'
            return value
        return wrapper
    return decorator


@make_html('i')
@make_html('del')
def get_text(text):
    return text
print(get_text(text='decorators are so cool!'))
# ----------------------------------------
import functools
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator
# ----------------------------------------
import functools
def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal start, end
            value = func(*args, **kwargs)
            start = max(0, start)
            end = min(len(value), end)
            return value[:start] + char * (end - start) + value[end:]
        return wrapper
    return decorator


import functools
def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return (value[:start] + char * (end - start) + value[end:])[:len(value)]
        return wrapper
    return decorator
# ----------------------------------------
import functools
def returns(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, datatype):
                raise TypeError
            return value
        return wrapper
    return decorator
# ----------------------------------------
import functools
def takes(*takes_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in [*args, *kwargs.values()]:
                if not isinstance(i, takes_args):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return decorator
# ----------------------------------------
import functools
def add_attrs(**attrs):
    def decorator(func):
        func.__dict__.update(attrs)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


import functools
def add_attrs(**attrs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        wrapper.__dict__ |= attrs
        return wrapper
    return decorator
# ----------------------------------------
import functools
def ignore_exception(*ignore_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ignore_args as err:
                print(f'Исключение {err.__class__.__name__} обработано')
#               print(f'Исключение {type(err).__name__} обработано')
            except Exception as err:  # these 2 strings
                raise err             # are not necessasry
        return wrapper
    return decorator
# ----------------------------------------
import functools
class MaxRetriesException(Exception):
    pass
def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            raise MaxRetriesException
        return wrapper
    return decorator
# ======================================== 9.9
from functools import partial
to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')
send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут....')
# ----------------------------------------
import sys
for line in sys.stdin.readlines():
    print(''.join(sorted(line.strip())))


from functools import lru_cache
import sys
@lru_cache
def sorted_cache(string):
    return ''.join(sorted(string))
for line in sys.stdin.readlines():
    print(''.join(sorted_cache(line.strip())))
# ----------------------------------------
from functools import lru_cache
@lru_cache
def ways(n):
    if n in (1, 2, 3):  # 0, 1, 1+1
        return 1
    if n == 4:  # 1+1+1 | 3
        return 2
    if n == 5:  # 1+1+1+1 | 1+1+1+3 | 3+1+1+1 | 4
        return 4
    return ways(n - 1) + ways(n - 3) + ways(n - 4)

print(ways(50))
# 9107509825
# ======================================== 10.1
numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
numbers_iter = iter(numbers)
for _ in range(3):
    next(numbers_iter)
print(next(numbers_iter))
# ----------------------------------------
numbers = [100, 70, 34, 45, 30, 83, 12, 83, -28, 49, -8, -2, 6, 62, 64, -22, -19, 61, 13, 5, 80, -17, 7, 3, 21, 73, 88, -11, 16, -22]
numbers_iter = iter(numbers)
for _ in range(len(numbers) - 1):
    next(numbers_iter)
print(next(numbers_iter))


iterator = iter(numbers)
*_, last = iterator
print(last)


numbers = iter(numbers)
while True:
    try:
        n = next(numbers)
    except StopIteration:
        print(n)
        break
# ======================================== 10.2
def filterfalse(predicate, iterable):
    return filter(lambda x: not predicate(x) if predicate else not bool(x), iterable)


from itertools import filterfalse
# ----------------------------------------
def transpose(matrix):
    return list(map(list, zip(*matrix)))


transpose = lambda matrix: list(map(list, zip(*matrix)))
# ----------------------------------------
def get_min_max(data):
    return None if not data else (data.index(min(data)), data.index(max(data)))
# ----------------------------------------
def starmap(func, iterable):
    return map(func, *zip(*iterable))


from itertools import starmap
# ----------------------------------------
def get_min_max(iterable):
    iterator = iter(iterable)
    try:
        item = next(iterator)
    except StopIteration:
        return None
    min_, max_ = item, item
    while True:
        try:
            item = next(iterator)
            if item < min_:
                min_ = item
            if item > max_:
                max_ = item
            # min_ = min(min_, item)  # min / maxre written with C,
            # max_ = max(max_, item)  # but very few args in this case so it works slower
        except StopIteration:
            break
    return min_, max_


import copy
def get_min_max(i):
    a = copy.deepcopy(i)    
    if sum(copy.deepcopy(i)):
        return min(a), max(i)
    else:
        return
# ======================================== 10.3
infinite_love = iter(lambda: 'i love beegeek!', '')
# ----------------------------------------
def is_iterable(obj):
    return True if '__iter__' in dir(obj) else False


def is_iterable(obj):
    return '__iter__' in dir(obj)


def is_iterable(obj):
    return hasattr(obj, '__iter__')


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


from typing import Iterable
def is_iterable(obj):
    return isinstance(obj, Iterable)
# ----------------------------------------
def is_iterator(obj):
    return '__next__' in dir(obj)


from typing import Iterator
def is_iterator(obj):
    return isinstance(obj, Iterator)
# ----------------------------------------
from random import randint
def random_numbers(left, right):
    def closure():
        return randint(left, right)
    return iter(closure, left - 1)
# ======================================== 10.4
class Repeater:
    def __init__(self, obj):
        self.obj = obj
    def __iter__(self):
        return self
    def __next__(self):
        return self.obj
# ----------------------------------------
class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
    def __iter__(self):
        return self
    def __next__(self):
        if self.times == 0:
            raise StopIteration
        self.times -= 1    
        return self.obj
# ----------------------------------------
class Square:
    def __init__(self, n):
        self.n = n
        self.start = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.n:
            self.start += 1
            return self.start ** 2
        else:
            raise StopIteration


class Square:
    def __init__(self, n):
        self.it = iter(range(1, n+1))
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.it)**2
# ----------------------------------------
class Fibonacci:
    def __init__(self):
        self.first = 1
        self.second = 0
    def __iter__(self):
        return self
    def __next__(self):
        value = self.first + self.second
        self.first = self.second
        self.second = value
        return value


class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
# ----------------------------------------
class PowerOf:
    def __init__(self, number):
        self.number = number
        self.power = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.power += 1
        return self.number ** self.power
# ----------------------------------------
class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = iter(data)
    def __iter__(self):
        return self
    def __next__(self):
        key = next(self.keys)
        return key, self.data[key]
# ----------------------------------------
class CardDeck:
    def __init__(self):
        self.suit = ('пик', 'треф', 'бубен', 'червей')
        self.rank = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        self.start = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < 51:
            self.start += 1
            return f'{self.rank[self.start % 13]} {self.suit[self.start // 13]}'
        else:
            raise StopIteration
# ----------------------------------------
class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter = iter(self.iterable)
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return next(self.iter)
        except:
            self.iter = iter(self.iterable)
            return next(self.iter)
# ----------------------------------------
from random import randint
class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > 0:
            self.n -= 1
            return randint(self.left, self.right)
        else:
            raise StopIteration


from random import randint
class RandomNumbers:    
    def __init__(self, left, right, n):
        self.data = (randint(left, right) for _ in range(n))
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.data)
# ----------------------------------------
class Alphabet:
    def __init__(self, language):
        self.language = language
        self.abc = {'en': 'abcdefghijklmnopqrstuvwxyz',
                    'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.iter = iter(self.abc[self.language])
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return next(self.iter)
        except:
            self.iter = iter(self.abc[self.language])
            return next(self.iter)
# en = range(ord('a'), ord('z') + 1)
# ru = range(ord('а'), ord('я') + 1)
# ----------------------------------------
class Xrange:
    def __init__(self, start, end, step=1):
        self.type_ = (int, float)[float in (type(start), type(step))]
        self.start = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        value = self.type_(self.start)
        if (self.step > 0 and self.start < self.end) or (self.step < 0 and self.start > self.end):
            self.start += self.step
            return value
        else:
            raise StopIteration
# ======================================== 10.5
def simple_sequence():
    number = 1
    while True:
        for _ in range(number):
            yield number
        number += 1
# ----------------------------------------
def alternating_sequence(count=None):
    if count is None:
        number = 1
        while True:
            yield number if number % 2 else -number
            number += 1
    else:
        for number in range(1, count + 1):
            yield number if number % 2 else -number


def alternating_sequence(count=None):
    n = 0
    while n != count:
        n += 1
        yield n if n % 2 else -n
# ----------------------------------------
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
def primes(left, right):
    for n in range(max(left, 2), right + 1):
        if is_prime(n):
            yield n


from sympy import isprime
def primes(left, right):
    yield from (i for i in range(left, right + 1) if isprime(i))
# ----------------------------------------
def reverse(sequence):
    for n in range(len(sequence) - 1, -1, -1):
        yield sequence[n]


def reverse(sequence):
    for i in sequence[::-1]:
        yield i
# ----------------------------------------
from datetime import date, timedelta
def dates(start, count=None):
    number = 0
    while number != count:
        yield start
        if start == date(9999, 12, 31):
            return
        start += timedelta(days=1)
        number += 1


from datetime import date, timedelta
def dates(start, count=None):
    count = count or (date.max - start).days + 1
    for i in range(count):
        yield start + timedelta(days=i)
# ----------------------------------------
def card_deck(suit):
    suits = ['пик', 'треф', 'бубен', 'червей']
    suits.remove(suit)
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
    while True:
        for s in suits:
            for r in ranks:
                yield f'{r} {s}'


def card_deck(suit):
    return (f'{j} {i}' 
            for _ in iter(lambda: 1, 0) 
            for i in 'пик треф бубен червей'.split() 
            for j in '2 3 4 5 6 7 8 9 10 валет дама король туз'.split() 
            if i != suit)
# ----------------------------------------
def matrix_by_elem(matrix):
    for row in matrix:
        yield from row
# ----------------------------------------
def palindromes():
    num = 1
    while True:
        if str(num) == ''.join(reversed(str(num))):
#       if str(num) == str(num)[::-1]:
            yield num
        num += 1


def palindromes():
    yield from (i for i, _ in enumerate(iter(bool, True), 1) if str(i) == str(i)[::-1])


# infinite iterator
iter(bool, True)
iter(int, 1)
iter(lambda: 1, 0)
# ----------------------------------------
def flatten(nested_list):
    for obj in nested_list:
        if isinstance(obj, int):
            yield obj
        else:
            yield from flatten(obj)


def flatten(nested_list):
    for i in nested_list:
        yield from [i] if isinstance(i, int) else flatten(i)
# ======================================== 10.6
def cubes_of_odds(iterable):
    return (number ** 3 for number in iterable if number % 2)
# ----------------------------------------
def is_prime(number):
    return not any(i for i in range(2, number) if (number % i) == 0) and number != 1


from sympy import isprime as is_prime
# ----------------------------------------
def count_iterable(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count


def count_iterable(iterable) -> int:
    return sum(1 for _ in iterable)
# ----------------------------------------
def all_together(*args):
    return (i for iterable in args for i in iterable)
# ----------------------------------------
def interleave(*args):
    return (i for iterable in zip(*args) for i in iterable)


def interleave(*args):
    return (
        i
        for iterable in zip(*args)
        for i in iterable
    )


def interleave(*args):
    for iterable in zip(*args):
        yield from iterable
# ======================================== 10.7
from collections import namedtuple
Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])
persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]
men = (man for man in persons
       if man.nationality == 'Swedish'
       and man.sex == 'male'
       and man.death == 0)
yangest_man = max(men, key=lambda x: x.birth)
print(yangest_man.name)


swed = (i for i in persons if i.nationality == 'Swedish')
alive_swed = (i for i in swed if i.death == 0)
men_alive_swed = (i for i in alive_swed if i.sex == 'male')
young_men_alive_swed = max(men_alive_swed, key=lambda x: x.birth)
print(young_men_alive_swed.name)
# ----------------------------------------
def parse_ranges(ranges):
    for i, j in (map(int, i.split('-')) for i in (ranges.split(','))):
        yield from range(i, j + 1)


def parse_ranges(ranges: str):
    for r in ranges.split(","):
        start, end = map(int, r.split("-"))
        yield from range(start, end + 1)


def parse_ranges(ranges):
    return (j 
            for i in ranges.split(',') 
            for a, b in [i.split('-')] 
            for j in range(int(a), int(b) + 1))
# ----------------------------------------
def filter_names(names, ignore_char, max_names):
    for name in names:
        if (not name.lower().startswith(ignore_char.lower())
                and max_names > 0
                and name.isalpha()):
            max_names -= 1
            yield name


def filter_names(names, ignore_char, max_names):
    filtred_char = (name for name in names if not name.lower().startswith(ignore_char.lower()))
    filtred_dig = (name for name in filtred_char if name.isalpha())
    return (name for idx, name in enumerate(filtred_dig) if idx < max_names)
# ----------------------------------------
import csv
with open('data.csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_dicts = (dict(zip(file_headers, data)) for data in line_values)
    print(sum(int(line['raisedAmt']) for line in line_dicts if line['round'] == 'a'))


import csv
with open('data.csv', encoding='utf8') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(sum(int(line[1]) for line in reader if line[3] == 'a'))
# ----------------------------------------
from datetime import date, timedelta
def years_days(year):
    start = date(year=year, month=1, day=1)
    finish = date(year=year, month=12, day=31)
    while start <= finish:
        yield start
        start += timedelta(days=1)


from datetime import date, timedelta
def years_days(year: int):
    start = date(year, 1, 1)
    while start.year == year:
        yield start
        start += timedelta(days=1)


from datetime import date, timedelta
from calendar import isleap 
def years_days(year):
    n_days = 365 + isleap(year)
    return (date(year, 1, 1) + timedelta(days=i) for i in range(n_days))
# ----------------------------------------
def nonempty_lines(file):
    with open(file, encoding='utf8') as file:
        return (line.strip() if len(line.strip()) <= 25 else '...'
                for line in file.readlines()
                if line.strip())
#       yield from (...)
# ----------------------------------------
def txt_to_dict():
    with open('planets.txt', encoding='utf8') as file:
        for block in file.read().split('\n\n'):
            yield dict(line.split(' = ') for line in block.split('\n'))
# ----------------------------------------
def unique(iterable):
    set_ = set()
    for i in iterable:
        if i not in set_:
            set_.add(i)
            yield i


def unique(numbers):
    yield from (dict.fromkeys(numbers))


def unique(iterable):
    yield from {i: 0 for i in iterable}
# ----------------------------------------
def stop_on(iterable, obj):
    for i in iterable:
        if i == obj:
            break
        yield i


def stop_on(iterable, obj):
    it = iter(iterable)
    return iter(lambda: next(it), obj)
# ----------------------------------------
def with_previous(iterable):
    if not iterable:
        return None
    it = iter(iterable)
    last = next(it)
    yield (last, None)
    for i in it:
        yield (i, last)
        last = i


def with_previous(iterable):
    prev_elem = None
    for elem in iterable:
        yield elem, prev_elem
        prev_elem = elem
or
def with_previous(iterable, prev_elem=None):
    for elem in iterable:
        yield elem, prev_elem
        prev_elem = elem


def with_previous(iterable):
    prev = None
    return ((i, prev, prev := i)[:-1] for i in iterable)   
# ----------------------------------------
def pairwise(iterable):
    if not iterable:
        return None
    it = iter(iterable)
    prev_elem = next(it)
    yield from ((prev_elem, elem, prev_elem := elem)[:-1] for elem in it)
    yield prev_elem, None


def pairwise(iterable):
    it = iter(iterable)
    i = next(it, None)
    while i != None:
        i, prev = next(it, None), i
        yield prev, i


def pairwise(iterable):
    it = iter(iterable)
    start = next(it, None)
    while not start is None:
        yield (start, start := next(it, None))
# ----------------------------------------
def around(iterable):
    if not iterable:
        return None
    it = iter(iterable)
    prev_elem = None
    curr_elem = next(it)
    yield from ((prev_elem, curr_elem, elem, prev_elem := curr_elem, curr_elem := elem)[:-2] for elem in it)
    yield prev_elem, curr_elem, None


def around(iterable):
    it = iter(iterable)
    a = None
    b = next(it, None)
    c = next(it, None)
    while b != None:
        yield a, b, c
        a, b, c = b, c, next(it, None)
# ======================================== 10.8
from itertools import count
def tabulate(func):
    return map(func, count(1))
# ----------------------------------------
from itertools import accumulate
import operator
def factorials(n):
    return accumulate(range(1, n + 1), operator.mul)
# ----------------------------------------
from itertools import count, cycle
from string import ascii_uppercase
def alnum_sequence():
    for i in cycle(zip(count(1), ascii_uppercase)):
        yield from i
# ----------------------------------------
from itertools import zip_longest
def roundrobin(*args):
    for tuple_ in zip_longest(*args, fillvalue=':)'):
        yield from (i for i in tuple_ if i != ':)')
# ======================================== 10.9
from itertools import dropwhile
def drop_while_negative(iterable):
    return dropwhile(lambda x: x < 0, iterable)
# ----------------------------------------
from itertools import dropwhile
def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)
# ----------------------------------------
def first_true(iterable, predicate=None):
    for i in iter(iterable):
        if (predicate if predicate else bool)(i):
            return i


def first_true(iterable, predicate=None):
    for i in filter(predicate, iter(iterable)):
        return i


def first_true(iterable, predicate):
    return next(filter(predicate, iterable), None)
# ----------------------------------------
from itertools import dropwhile, takewhile, filterfalse, compress, islice
def take(iterable, n):
    return islice(iterable, n)


from itertools import islice as take
# ----------------------------------------
from itertools import dropwhile, takewhile, filterfalse, compress, islice
def take_nth(iterable, n):
    try:
        return next(islice(iterable, n - 1, n))
    except StopIteration:
        return None


from itertools import islice

def take_nth(iterable, n):
    return next(islice(iterable, n-1, None), None)
# ----------------------------------------
from itertools import dropwhile, takewhile, filterfalse, compress, islice
def first_largest(iterable, n):
    return next(dropwhile(lambda x: x[1] <= n, enumerate(iterable, 0)), (-1,))[0]
# ======================================== 10.10
from itertools import chain
def sum_of_digits(iterable):
    return sum(map(int, chain.from_iterable(map(str, iterable))))
# ----------------------------------------
from itertools import starmap, pairwise
def is_rising(iterable):
    return all(starmap(lambda a, b: a < b, pairwise(iterable)))


from itertools import pairwise
def is_rising(iterable):
    return all(a < b for a, b in pairwise(iterable))
# ----------------------------------------
from itertools import pairwise
def max_pair(iterable):
    return max(a + b for a, b in pairwise(iterable))


rom itertools import pairwise
def max_pair(iterable):
    return max(map(sum, pairwise(iterable)))
# ----------------------------------------
from itertools import chain, tee
def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))
# ----------------------------------------
from itertools import chain, islice, zip_longest
def grouper(iterable, n):
    iterator = iter(iterable)
    first = next(iterator, None)
    while first:
        yield tuple(islice(chain.from_iterable(zip_longest([first] + [*islice(iterator, 0, n - 1)], range(n))), 0, None, 2))
        first = next(iterator, None)


from itertools import zip_longest, repeat
def grouper(iterable, n):
    yield from zip_longest(*repeat(iter(iterable), n))


from itertools import zip_longest
def grouper(iterable, n):
    return zip_longest(*[iter(iterable)] * n)
# ======================================== 10.11
from collections import namedtuple
from itertools import groupby
Person = namedtuple('Person', ['name', 'age', 'height'])
persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

for key, group in groupby(sorted(persons, key=lambda x: (x[2], x[0])), key=lambda x: x.height):
    print(f'{key}: {", ".join([i.name for i in group])}')


persons.sort(key=lambda x: (x.height, x.name))
groups = groupby(persons, key=lambda x: x.height)
for key, tpl in groups:
    print(f'{key}: {", ".join(i.name for i in tpl)}')
# ----------------------------------------
from collections import namedtuple
from itertools import groupby
Student = namedtuple('Student', ['surname', 'name', 'grade'])
students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11), Student('Кодзаев', 'Георгий', 10),
            Student('Набокова', 'Алиса', 11), Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
            Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10), Student('Капустин', 'Илья', 11),
            Student('Гудцев', 'Таймураз', 11), Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
            Student('Елькина', 'Мария', 11),Student('Макоев', 'Руслан', 11), Student('Албегов', 'Хетаг', 11),
            Student('Щербак', 'Илья', 10), Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
            Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11), Student('Мусиков', 'Андраник', 11),
            Student('Гадзиев', 'Георгий', 11), Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
            Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10), Student('Акоева', 'Лера', 11)]

names = [student.name for student in students]
name_group = {key: sum(1 for _ in group) for key, group in groupby(sorted(names))}
print(max(name_group, key=name_group.get))


print(Counter(i.name for i in students).most_common()[0][0])
# ----------------------------------------
from itertools import groupby
for key, group in groupby(sorted(input().split(), key=len), key=len):
    print(f'{key} -> {", ".join(sorted(group))}')


from itertools import groupby
list_ = sorted(input().split(), key=lambda x: (len(x), x))
for key, group in groupby(list_, key=len):
    print(f'{key} -> {", ".join(list(group))}')
# ----------------------------------------
from itertools import groupby
tasks = [('Отдых', 'поспать днем', 3),
        ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
        ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
        ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
        ('Отдых', 'погулять вечером', 4),
        ('Курс по ооп', 'обсудить темы', 1),
        ('Урок по groupby', 'добавить задачи на программирование', 3),
        ('Урок по groupby', 'написать конспект', 1),
        ('Отдых', 'погулять днем', 2),
        ('Урок по groupby', 'добавить тестовые задачи', 2),
        ('Уборка', 'убраться в ванной', 2),
        ('Уборка', 'убраться в комнате', 1),
        ('Уборка', 'убраться на кухне', 3),
        ('Отдых', 'погулять утром', 1),
        ('Курс по ооп', 'обсудить задачи', 2)]

tasks.sort(key=lambda x: (x[0], x[2]))
for key, group in groupby(tasks, key=lambda x: x[0]):
    print(f'{key}:')
    for i in group:
        print(f'    {i[2]}. {i[1]}')
#       print(f'{i[2]:5}. {i[1]}')
    print()
# ----------------------------------------
from itertools import groupby
def group_anagrams(words):
    list_ = sorted([(sorted(w), w) for w in words])
    return (tuple(i[1] for i in group) for _, group in groupby(list_, key=lambda x: x[0]))


from itertools import groupby
def group_anagrams(words):
    return (tuple(i) for _, i in groupby(sorted(words, key=sorted), key=sorted))
# ----------------------------------------
def ranges(numbers):
    l = []
    d = [numbers[0], numbers[0]]
    for i in numbers:
        if i - d[1] <= 1:
            d[1] = i
        else:
            l.append(tuple(d))
            d = [i, i]
    l.append(tuple(d))
    return l


from itertools import groupby
def ranges(numbers):
    result = []
    for _, group in groupby(numbers, key=lambda n: n - numbers.index(n)):
        group = tuple(group)
        group = group[0], group[-1]
        result.append(group)
    return result


from itertools import groupby
def ranges(a):
    c = groupby(a, key=lambda x: x - a.index(x))
    b = (tuple(v) for k, v in c)
    return [(i[0], i[-1]) for i in b]
# ======================================== 10.12
from itertools import permutations, combinations, combinations_with_replacement
print(*map(lambda x: ''.join(x), sorted(set(permutations(input())))), sep='\n')
# ----------------------------------------
from itertools import permutations, combinations, combinations_with_replacement
wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
set_ = set()
for i in range(1, 14):
    set_ |= set(filter(lambda x: sum(x) == 100, combinations(wallet, i)))
#   set_.update(filter(lambda x: sum(x) == 100, combinations(wallet, i)))
print(len(set_))
# ----------------------------------------
from itertools import permutations, combinations, combinations_with_replacement
wallet = [100, 50, 20, 10, 5]
set_ = set()
for i in range(1, 21):
    set_.update(filter(lambda x: sum(x) == 100, combinations_with_replacement(wallet, i)))
print(len(set_))
# ----------------------------------------
from collections import namedtuple
from itertools import combinations
Item = namedtuple('Item', ['name', 'mass', 'price'])
items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

weight = int(input())
set_ = set()
for i in range(1, len(items) + 1):
    set_.update(filter(lambda x: sum(i.mass for i in x) <= weight, combinations(items, i)))
backpack = max((sum(i.price for i in tuple_), tuple_) for tuple_ in set_)[1] if set_ else None
if backpack:
    print(*[i.name for i in sorted(backpack)], sep='\n')
else:
    print('Рюкзак собрать не удастся')
# ----------------------------------------
from string import ascii_lowercase
from itertools import product
letters = ascii_lowercase[:8]
digits = [1, 2, 3, 4, 5, 6, 7, 8]

for a, b in product(letters, digits):
    print(f'{a}{b}', sep='', end=' ')


for card in product(letters, digits):
    print(*card, sep='', end=' ')
# ----------------------------------------
from itertools import product, repeat
def password_gen():
    for time in product(range(10), repeat=3):
#   for time in product(range(10), range(10), range(10)):
        yield ''.join(map(str, time))
#       yield f'{i}{j}{k}'


def password_gen():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield str(i) + str(j) + str(k)
# ----------------------------------------
from itertools import product, repeat
for prod in product(list('0123456789ABCDEF')[:int(input())], repeat=int(input())):
    print(*prod, sep='', end=' ')
# ======================================== 11.1
import re
print(*re.findall(r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}', input()), sep='\n')
# ----------------------------------------
regex = r'beegeek'
# ----------------------------------------
regex = r'...\....'
# ----------------------------------------
regex = r'1\d\d'
# ----------------------------------------
regex = r'\d{3}-\d{3}-\d{4}'
# ======================================== 11.2
regex = r'ca[rtb]'
# ----------------------------------------
regex = r'[0-9A-F]'
# ----------------------------------------
regex = r'[a-zA-Z]\d{4}'
# ----------------------------------------
regex = r'[a-z][0-9][a-z][A-Z][A-Z]'
# ----------------------------------------
regex = r'[0-9][aeiouy][^bcDF][^ ][^AEIOUY][^.,]'
# ----------------------------------------
regex = r'[123][012][12x][03aA][xsu][.,]'
# ----------------------------------------
regex = r'[+]7\d{10}|[+]7[(]\d{3}[)]\d{7}|[+]7[(]\d{3}[)]-\d{3}-\d{2}-\d{2}|[+]7 \d{3} \d{3} \d{2} \d{2}'


regex = r'\+7\d{10}|' \
        r'\+7\(\d{3}\)\d{7}|' \
        r'\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}|' \
        r'\+7 \d{3} \d{3} \d{2} \d{2}'


regex = (
    r'\+7\d{10}|'
    r'\+7\(\d{3}\)\d{7}|'
    r'\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}|'
    r'\+7 \d{3} \d{3} \d{2} \d{2}'
)


r = r'\+7xxxxxxxxxx|\+7\(xxx\)xxxxxxx|\+7\(xxx\)-xxx-xx-xx|\+7 xxx xxx xx xx'.replace('x', '\d')
regex = r
# ----------------------------------------
regex = r'\d{2}[/]\d{2}[/]\d{4}|\d{2}[.]\d{2}[.]\d{4}|\d{4}[/]\d{2}[/]\d{2}|\d{4}[.]\d{2}[.]\d{2}'
# ----------------------------------------
regex = r'[01][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]'
# ======================================== 11.3
regex = r'[A-Z]{5}[0-9]{4}[A-Z]'
# ----------------------------------------
regex = r'<!--.*?-->'
# ----------------------------------------
regex = r'[a-z]{,3}[0-9]{2,8}[A-Z]{3,}'
# ----------------------------------------
regex = r'[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}'
# ======================================== 11.4
regex = r'\b[aA]n?\b'
# ----------------------------------------
regex = r'\b[A-Z]+\b'
# ----------------------------------------
regex = r'\b[A-Z]\w*\b'
# ----------------------------------------
regex = r'.*\(.*\).*'
# ----------------------------------------
regex = r'^\d{2,}[a-z]*[A-Z]*$'
# ----------------------------------------
regex = r'^[a-zA-Z]*s$'
# ----------------------------------------
regex = r'^[a-zA-Z24680]{40}[13579 ]{5}$'
# ----------------------------------------
regex = r'^M[rs]\.[a-zA-Z]+$|^Mrs\.[a-zA-Z]+$|^[DE]r\.[a-zA-Z]+$'


regex = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-z]+$'
# ----------------------------------------
regex = r'^[0-9]{1,2}[a-zA-Z]{3,}\.{,3}$'
# ======================================== 11.5
regex = r'\d{5}(-\d{4})?'
# ----------------------------------------
regex = r'([2-9]\d{2}|\([2-9]\d{2}\))[ -][2-9]\d{2}-\d{4}'
# ----------------------------------------
regex = r'(beegeek(geek)*)+'
# ----------------------------------------
regex = r'([a-z])(\w)([A-Z])\1\2\3'
# ----------------------------------------
regex = r'(ok){3,}'
# ----------------------------------------
regex = r'(.)(.)(.)(.)(.)\4\3\2\1'
# ----------------------------------------
regex = r'\w*([a-zA-Z]+)\w*\1\w*'
# ----------------------------------------
regex = r'(\d{8}|(\d{2}-){3}\d{2})'
# ----------------------------------------
regex = r'(\d{8}|(\d{2}(-|---|\.))(\d{2}\3){2}\d{2})'


regex = r'\d{2}((-|---|\.)?)(\d{2}\1){2}\d{2}'


regex = r'\d{2}(-|---|\.|)(\d{2}\1){2}\d{2}'
# ----------------------------------------
regex = r'\b(\w+\b) +\1\b'
# ======================================== 11.6
import re, sys
pattern = r'(\d{1,3})([ -])(\d{1,3})\2(\d{4,10})'
for line in sys.stdin:
    match = re.search(pattern, line)
    print(f'Код страны: {match.group(1)}, Код города: {match.group(3)}, Номер: {match.group(4)}' if match else None)

import re, sys
pattern = r"(?P<country>\d{1,3})([ -]?)(?P<city>\d{1,3})\2(?P<number>\d{4,10})"
for number in map(str.rstrip, sys.stdin):
    match = re.fullmatch(pattern, number)
    groups = match.groupdict()
    print(f"Код страны: {groups['country']}, Код города: {groups['city']}, Номер: {groups['number']}")
# ----------------------------------------
import re, sys
pattern = r'^_\d+[a-zA-Z]*_?$'
for line in sys.stdin:
    match = re.fullmatch(pattern, line.strip())
    print(True if match else False)
# ----------------------------------------
import re, sys
pattern = r'\b(\w+)\1\b'
for line in sys.stdin:
    match = re.fullmatch(pattern, line.strip())
    print(match.group()) if match else None
# ----------------------------------------
import re, sys
pattern1 = r'.*bee.*bee.*'
pattern2 = r'\bgeek\b'
m1, m2 = 0, 0
for line in sys.stdin:
    m1 += 1 if re.findall(pattern1, line) else 0
    m2 += 1 if re.findall(pattern2, line) else 0
print(m1, m2, sep='\n')
# ----------------------------------------
import re, sys
pattern1 = r'.+beegeek.+'
pattern2 = r'^beegeek.+|.+beegeek$|^beegeek$'
pattern3 = r'^beegeek.*beegeek$'
res = 0
for line in sys.stdin:
    if re.search(pattern3, line.strip()):
        res += 3
        continue
    if re.search(pattern2, line.strip()):
        res += 2
        continue
    if re.search(pattern1, line.strip()):
        res += 1
        continue
print(res)
# ----------------------------------------
import re, sys
pattern = r'^(Здравствуйте|Доброе утро|Добрый день|Добрый вечер).*'
for line in sys.stdin:
    match = re.fullmatch(pattern, line, flags=re.IGNORECASE)
    print(True if match else False)
# ----------------------------------------
import re, sys
pattern = r'.*beegeek.*'
print(sum([1 if re.search(pattern, line, flags=re.IGNORECASE) else 0 for line in sys.stdin]))
# ======================================== 11.7
article = '''Stepik (до августа 2016 года Stepic) — это образовательная платформа и конструктор онлайн-курсов!

Первые образовательные материалы были выпущены на Stepik 3 сентября 2013 года.
В январе 2016 года Stepik выпустил мобильные приложения под iOS и Android. В 2017 году разработаны мобильные приложения для изучения ПДД в адаптивном режиме для iOS и Android...

На октябрь 2020 года на платформе зарегистрировано 5 миллионов пользователей!
Stepik позволяет любому зарегистрированному пользователю создавать интерактивные обучающие уроки и онлайн-курсы, используя видео, тексты и разнообразные задачи с автоматической проверкой и моментальной обратной связью. 

Проект сотрудничает как с образовательными учреждениями, так и c индивидуальными преподавателями и авторами.  
Stepik сегодня предлагает онлайн-курсы от образовательных организаций, а также индивидуальных авторов!

Система автоматизированной проверки задач Stepik была использована в ряде курсов на платформе Coursera, включая курсы по биоинформатике от Калифорнийского университета в Сан-Диего и курс по анализу данных от НИУ «Высшая школа экономики»...

Stepik также может функционировать как площадка для проведения конкурсов и олимпиад, среди проведённых мероприятий — отборочный этап Олимпиады НТИ (2016—2020) (всероссийской инженерной олимпиады школьников, в рамках программы Национальная технологическая инициатива), онлайн-этап акции Тотальный диктант в 2017 году, соревнования по информационной безопасности StepCTF-2015...'''

import re
pattern1 = r'^Stepik.*'
pattern2 = r'\.\.\.$|!$'
m1, m2 = 0, 0
for line in article.split('\n'):
    m1 += 1 if re.findall(pattern1, line, flags=re.IGNORECASE | re.MULTILINE) else 0
    m2 += 1 if re.findall(pattern2, line, flags=re.IGNORECASE | re.MULTILINE) else 0
print(m1, m2, sep='\n')


print(len(re.findall('^stepik', article, re.I|re.M)))
print(len(re.findall('!$|\.\.\.$', article, re.M)))
# ----------------------------------------
import re
string = input()
subword = input()
pattern = fr'\B({subword})\B'
print(len(re.findall(pattern, string)))
# ----------------------------------------
import re
string = input()
word = input()
pattern = fr'\b({word})\b'
print(len(re.findall(pattern, string)))
# ----------------------------------------
import re
word = input()
string = input()
pattern = fr'\b{word[:-2]}[zs]e\b'
print(len(re.findall(pattern, string, flags=re.I)))
# ----------------------------------------
import re
word = input()
string = input()
pattern = fr'\b({word.replace("or", "our")}|{word.replace("our", "or")})\b'
print(len(re.findall(pattern, string, flags=re.I)))
# ----------------------------------------
import re
def abbreviate(string):
    pattern = fr'[A-Z]|\b[a-zA-Z]'
    return ''.join(re.findall(pattern, string)).upper()
# ----------------------------------------
import re, sys
pattern = r'<a href="(.+)">(.+)</a>'
for line in sys.stdin:
    for i in re.findall(pattern, line):
        print(*i, sep=', ')
# ----------------------------------------
import re, sys
from itertools import chain
pattern_tag = r'<\w+.*?>'
pattern_attr = r'<(\w*)\b|\b(\w+(-?\w*)*)='
dict_ = {}
for line in sys.stdin:
    for i in re.findall(pattern_tag, line):
        tag = list(filter(None, chain.from_iterable(re.findall(pattern_attr, i))))
        dict_[tag[0]] = dict_.get(tag[0], []) + tag[1:]
for key, value in sorted(dict_.items()):
    print(f'{key}: {", ".join(sorted(set(value)))}')


import re
res = {}
for line in open(0):
    for tag, params in re.findall(r'<(\w+)(.*?)>', line):
        res.setdefault(tag, set()).update(re.findall(r'([\w-]+)=', params))
for key in sorted(res):
    print(f'{key}: {", ".join(sorted(res[key]))}')
# ======================================== 11.8
import re
def normalize_jpeg(filename):
    return re.sub(r'\.(jpg|jpeg)$', r'.jpg', filename, flags=re.I)


import re
def normalize_jpeg(filename: str) -> str:
    return re.sub(r"jpe?g$", "jpg", filename, flags=re.I)
# ----------------------------------------
import re
def normalize_whitespace(string):
    return re.sub(r' +', r' ', string)
# ----------------------------------------
import re, keyword
def func(match_obj):
    word = match_obj.group(0)
    return '<kw>' if word.lower() in map(str.lower, keyword.kwlist) else word
print(re.sub(r'\w+', func, input()))


import re, keyword
keys = '|'.join(keyword.kwlist)
print(re.sub(fr"\b({keys})\b", r'<kw>', input(), flags=re.I))
# ----------------------------------------
import re
print(re.sub(r'\b(\w)(\w)', r'\2\1', input()))
# ----------------------------------------
import re
def func(match_obj):
    return match_obj[2] * int(match_obj[1])
string, n = input(), 1
while n:
    string, n = re.subn(r'(\d+)\((\w+)\)', func, string)
print(string)


import re
string, n = input(), 1
while n:
    string, n = re.subn(r'(\d+)\((\w+)\)', lambda x: x[2] * int(x[1]), string)
print(string)
# ----------------------------------------
import re
string, n = input(), 1
while n:
    string, n = re.subn(r'(\b(\w+)\b)\W+(\1)\b', r'\1', string)
#   string, n = re.subn(r'(\b(\w+)\b)\W+(\1)\b', lambda x: x[1] if x[1] == x[3] else x[0], string)
print(string)


import re
print(re.sub(r"(\b\w+)(\W+\1)+\b", r'\1', input()))
# ----------------------------------------
import re, sys
string = sys.stdin.read()
string = re.sub(r'^ *""".*?""" *$\n', r'', string, flags=re.DOTALL | re.M)
string = re.sub(r'^ *#.*$\n', r'', string, flags=re.M)
string = re.sub(r'#.*$', r'', string, flags=re.M)
print(string)


import re, sys
regex = r'\n#.*?$|' \
        r'\s*""".*?"""|' \
        r'\n? *#.*?$'
s = sys.stdin.read()
print(re.sub(regex, '', s, flags=re.S | re.M))


import re
print(re.sub(r' *?""".*?""".*?\n|  #.*?$| *#.*?$\n', r'', open(0).read(), flags=re.S | re.M))
# ======================================== 11.9
import re
print(*re.split(r'\s*[,;.]\s*', input()))
# ----------------------------------------
import re
print(*re.split(r'\s*(?:\||\&|and|or)\s*', input()), sep=', ')
#print(*re.split(r'\s*(?:[|&]|and|or)\s*', input()), sep=', ')
# ----------------------------------------
import re
def multiple_split(string, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    return re.split(pattern, string)
# ----------------------------------------
import re
pos, endpos = map(int, input().split())
string = input()
regex_obj = re.compile(r'\d+')
print(sum(map(int, regex_obj.findall(string, pos, endpos))))
# ========================================
