def find_y_words(filename):
    with open(filename, 'r') as words:
        sol = [line.strip() for line in words if line[0] == 'y' and len(line)>=11]

    len_sol = len(sol)
    return len_sol, sol

find_y_words('words.txt')

a = [(word,ch) for word in ['one', 'two', 'three', 'four'] for ch in 'aeiou' if ch in word]

b = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if (x**2 + y**2) == z**2]


def find_largest_item_and_pos(lst):
    largest = lst[0]
    pos = 0
    for i, item in enumerate(lst):
        if item > largest:
            largest, pos = item, i

    return pos, largest

find_largest_item_and_pos([3,6,2,6,7,8,23,999,35])

import collections
#named tuples
Person = collections.namedtuple('Person', 'name age gender')

bob = Person(name='Bob', age=30, gender='male')
jane = Person(name='Jane', age=29, gender='female')
susan = Person('Susan', 39, 'female')


Shopping = {'milk': 122333, 'eggs': 3, 'bread': 2}
# for w in Shopping:
    # print('%5s | %s' % (Shopping[w], w))

import string

t = (12, 3.14159, 'ducks')
print(string.digits*3)
print('%-10.5d%-10.5f%-10.5s' % t)
print('%10d%10f%10s' % t)
print('%10.5d%10.5f%10.5s' % t)


('{} {} {}'.format(12, 3.14159, 'ducks'))

lst = [1,2,3,4,5,6,7,8,9]
odds = [x for x in lst if x%2==1]
sorted_fruit = [x for rem in range(2,-1,-1) for x in lst if x%2==rem]
print(sorted_fruit)
