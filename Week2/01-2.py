import math
import os

# Conditional Statements Example
x = 150
threshold = 100
if x > threshold:
    print("x is too large!")
else:  
    print("x is within the limit.")

# Another method:

condition = x > threshold and x < threshold * 2
if condition:
    print("x is too large!")
else:  
    print("x is within the limit.")

file = "data.txt"
if os.path.exists(file):
    print(f"{file} exists.")
else:
    print(f"{file} does not exist.")    

# loops

for i in range(10): # from 0 to 9
    print(i)
print("Done")
for i in range(5, 15): # from 5 to 14
    print(i)
print("Done")
for i in range(0, 20, 2): # from 0 to 19, step by 2
    print(i)
print("Done")
for i in range(10, 0, -1): # from 10 to 1, step by -1
    print(i)
print("Done")

for i in range(5):
    if i == 3:
        continue # skip the rest of the loop when i is 3
    print(i)
print("Done")

for i in range(5):
    j = i * 2
    print(i)
    print(j)
print("Done")

# calculating sum
total = 0
for i in range(5): # from 0 to 4
    print(f'Adding {i} to total {total}')
    total += i # same as total = total + i
    print(total)

factorial = 1
for i in range(1, 6): # from 0 to 4
    print(f'Multiplying {i} to factorial {factorial}')
    factorial *= i # same as total = total + i
    print(factorial)

sum = 0
for i in range(1, 101): # from 1 to 100
    if i % 2 == 0: # if i is even
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
        sum += i

print(f'Sum of odd numbers from 1 to 100 is {sum}')
