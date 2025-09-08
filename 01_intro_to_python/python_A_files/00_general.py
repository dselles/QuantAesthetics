import math
import os

# #https://docs.python.org/3/tutorial/
# #https://docs.python.org/3/tutorial/introduction.html   #numbers/strings
# #https://docs.python.org/3/tutorial/controlflow.html  #if for functions


# #enough to edit scripts, debug find your way around and also process data
# #declare a variable
# a =5.6

# #each variable has a type internally
# a = 5 #int
# b = 0.5 #float
# c = "hello" #string
# d = [1,5] #list
# print(c.__class__)

# #basic math
# b = b - a * 2.0

# #b = c + a #ERROR string+int 

# #debug

# #calling a function
# d = math.cos(5.6) #import and use function
# print(d)


# #string [objects have properties]
# a = "hello how are you"
# a.capitalize()
# b = a.split(' ')
# #interpolated string
# f = f'a is equal to {a}'

# #becareful of escape sequences \n
# print("yes\no")



# #code blocks [grouping statements]
# #if
# a = -5
# if a>0:
#     print('a is positive') 
# else:
#     print('a is negative')


# if a>-10 and a<10:
#     print("in range")

# if a<=-10 or a>=10:
#     print("out of range")

# #for
# for i in range(14):
#     print(f'i = {i}')

# for i in range(4, 15):
#     print(f'i = {i}')

# total = 0
# for i in range(1, 15):
#     total += i
# print(total)

# total = sum(range(1, 15))

# #for lists
# l = [0.5, 0.6, 0.7, 1.2, 3.5, "hello", 4]

# for el in l:
#     print(el)

# for i, el in enumerate(l):
#     print(f'{i}th element is {el}')

# for i, el in enumerate(l):
#     l[i] = el*2
#     print(f'{i}th element is {l[i]}')

# #comprehension
# l = [el*2 for el in l]  

# l1 = [1, 5, 7, 3,6,2,2,4,0,7,3,5,7,2,7,8]
# l2 = []
# for el in l1:
#     if el>2:
#         l2.append(el)

# #list and string slices
# # +---+---+---+---+---+---+
# #  | P | y | t | h | o | n |
# #  +---+---+---+---+---+---+
# #  0   1   2   3   4   5   6
# # -6  -5  -4  -3  -2  -1
# word = "one two three four five"
# print(l1[2:3])
# print(word[0])
# print(word[-1])
# print(word[3:7])


# print(len(l1))
# print(len(l2))
# print(l2)




# #functions
# def foo(a ,b):
#     return a+b

# #annotations
# def foo2(a: float, b: float)->float:
#     return a+b

# def max(a, b):
#     if a>b:
#         return a
#     else:
#         return b

# def max3_a(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c 

# def max3_b(a,b,c):
#     if a>b and a>c:
#         return a
#     if b>c:
#         return b        
#     return c 

# def max3_c(a,b,c):
#     return max(max(a,b),c)



# e = (1,"hello") #tuple
# f = {"a":4} #dictionary
# g =  {5, 'u'} #set


# #os
# workDir = os.getcwd()  
# contents = os.listdir(workDir)
# #filepaths


file = open('vectors.csv', 'r')
contents = file.readlines()
file.close()

for line in contents:
    tokens = line.split(',')
    word = tokens[0]
    print(f'found word {word}')
    vector = [float(t) for t in tokens[1:]]
    print(f'with vector  = {vector}')
