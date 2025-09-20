# Assignments from Week 2 of Quantitative Aesthetics
# https://canvas.harvard.edu/courses/159074/assignments/989331

# Exercise 1: print [0][1][2][3][4]
# first method, using end=''
print("exercise 1:")
for i in range(5):
    # print('[' + str(i) + ']', end='')
    print(f'[{i}]', end='') # alternative using f-strings (format strings) and omits the new line at the end.
print() # print a new line at the end

# second method, adding to a string and printing at the end
row = ''
for i in range(5):
    col = f'[{i}]'
    row += col
print(row)

# Exercise 2: print a 2D grid
print("\nexercise 2:")
for i in range(5):
    row = f'{i}:'
    for j in range(5):
        col = f'[{i},{j}]'
        row += col
    print(row)

# In-class example for exercise 2 and 3
print("\nin-class example for exercise 2 and 3:")
for i in range(8):
    row =  f''
    for j in range(16):
        if (i*j)%3 == 0:
            row += '.'
        else:
            row += 'o'
    print(row)

# In-class example using copilot with comment prompt
print("\nCopilot example for exercise 2:")
# create a nested loop that generates a 5x5 grid of coordinates
for y in range(5):
    row = ''
    for x in range(5):
        col = f'[{x},{y}]'
        row += col
    print(row)

# Exercise 3: print a pattern of o's and .'s
print("\nexercise 3:")

for i in range(8):
    row = ''
    for j in range(16):
        break_pt = i
        if j < break_pt:
            row += 'o'
        else:
            row += '.'
    print(row)

# Exercise 4: print a different pattern of o's and .'s
print("\nexercise 4:")

res_x = 24
res_y = 8

for i in range(res_y):
    row = ''
    for j in range(res_x):
        if (i+j)%2 == 0:
            row += 'o'
        else:
            row += '.'
    print(row)

# Exercise 5: print a pattern of randomly selected forward or back slashes
print("\nexercise 5:")

res_x = 24
res_y = 8
import random

for i in range(res_y):
    row = ''
    for j in range(res_x):
        if random.random() > 0.5:
            row += '/'
        else:
            row += '\\'
    print(row)

# Exercise 6: print a pattern of random o's and .'s with a gradient along the x-axis
print("\nexercise 6:")

res_x = 24
res_y = 8

import random

for i in range(res_y):
    row = ''
    for j in range(res_x):
        if random.random() > (j/res_x):
            row += '.'
        else:
            row += 'o'
    print(row)

# Exercise Bonus: print a pattern of random o's and .'s with a radial gradient from the center
print("\nexercise bonus:")

res_x = 50
res_y = 20
center_x = res_x / 2
center_y = res_y / 2
#max_dist = ((center_x)**2 + (center_y)**2)**0.5 # Pythagorean theorem
max_dist = 15
import random

for i in range(res_y):
    row = ''
    for j in range(res_x):
        dist = ((j - center_x)**2 + (i - center_y)**2)**0.5
        if random.random() > (dist/max_dist):
            row += 'o'
        else:
            row += '.'
    print(row)
