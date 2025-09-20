import random

#α. row of numbers [0][1][2][3][4]...
print('Single row with 5 columns: [0][1][2][3][4]...\n\n')
row = ''
for j in range(5):
    row += f'[{j}]'
print(row)

print('')


#β. 2D grid of numbers [0,0][0,1][0,2]...
print('2D grid with 5 rows and 5 columns: [0,0][0,1][0,2]...\n\n')
columns = 5
rows = 5

for i in range(rows):
    row = ''
    for j in range(columns):
        row += f'[{i},{j}]'
    print(row)

print('')

#γ. 2D grid of characters with threshold condition
print('2D grid with threshold condition:\n\n')
columns = 20
rows = 10

for i in range(rows):
    row = ''
    for j in range(columns):
        if i>j:
            row += 'O'
        else:
            row += '.'
    print(row)

print('')

#δ. 2D grid of characters with checkered pattern
print('2D grid with checkered pattern:\n\n')
columns = 20
rows = 10

for i in range(rows):
    row = ''
    for j in range(columns):
        if (i+j) % 2 == 0:
            row += 'O'
        else:
            row += '.'
    print(row)

print('')

#ε. 2D grid of characters with random choice (50% probability)
print('2D grid with random choice (50% probability):\n\n')
columns = 40
rows = 10

for i in range(rows):
    row = ''
    for j in range(columns):
        if random.random() < 0.5:
            row += '/'
        else:
            row += '\\'
    print(row)

print('')

#ζ. 2D grid of characters with random choice (gradient probability)
print('2D grid with random choice (gradient probability):\n\n')
for i in range(rows):
    row = ''
    for j in range(columns):
        if random.random() < j/columns:
            row += 'O'
        else:
            row += '.'
    print(row)

print('')

#η. 2D grid of characters with random choice (equal probability) using random.choice()
print('2D grid with random choice (equal probability) using random.choice():\n\n')
elements = ['/', '\\']
for i in range(rows):
    row = ''
    for j in range(columns):
        row += random.choice(elements)
    print(row)

print('')


#θ. 2D grid of characters with random choice (weighted probability) using random.choices()
print('2D grid with random choice (weighted probability) using random.choice():\n\n')
elements = ['O', 'o', '.']
probabilities = [0.8, 0.15, 0.05]
columns = 40
rows = 10

for i in range(rows):
    row = ''
    for j in range(columns):
        chosen = random.choices(elements, probabilities)
        row += chosen[0]
    print(row)
