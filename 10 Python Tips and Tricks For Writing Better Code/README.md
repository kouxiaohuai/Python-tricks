1.
```python
condition = True

if condition:
    x = 1
else:
    x = 0

x = 1 if condition else 0

print(x)

```
2. 
```
num1 = 10000000000
num2 = 100000000

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(total)
print(f'{total:,}')

```
3. 
```
with open('test.txt', 'r') as f:
    for line in f:
        print(line)

```
4.
```
names = ['Corey', 'Chris', 'Dave', 'Travis']

index = 0
for name in names:
    print(index, name)
    index += 1

for index, name in enumerate(names):
    print(index, name)

```
5. 
```
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

```
6. 
```
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

for value in zip(names, heroes, universes):
    print(value)

```
7. 
```
a, b = (1, 2)

print(a)
print(b)

```
```
a, _ = (1, 2)

print(a)

```
```
a, b, *c = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)

```
```
a, b, *_ = (1, 2, 3, 4, 5)

print(a)
print(b)

```
```
a, b, *c, d = (1, 2, 3, 4, 5)

print(a)
print(b)
print(c)
print(d)

```
8. 
```
class Person:
    pass


person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, 'first', 'Corey')

setattr(person, first_key, first_val)

print(person.first)
print(getattr(person, 'first'))
print(getattr(person, first_key))

```
```
class Person:
    pass


person = Person()

person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

```
