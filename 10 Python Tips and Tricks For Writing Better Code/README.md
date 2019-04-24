1. 
condition = True
```
if condition:
    x = 1
else:
    x = 0
```
x = 1 if condition else 0

print(x)

2. 
```
num1 = 10000000000
num2 = 100000000
```
num1 = 10_000_000_000  
num2 = 100_000_000

total = num1 + num2

print(total)
print(f'{total:,}')

3. 
with open('test.txt', 'r') as f:
    for line in f:
        print(line)

4. 
names = ['Corey', 'Chris', 'Dave', 'Travis']
```
index = 0
for name in names:
    print(index, name)
    index += 1
```
for index, name in enumerate(names):
    print(index, name)

5. 
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
```
for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')
```
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

6. 
