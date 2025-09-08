#when discussing loops we saw that the general form is:
#for iterator in iterable:
#and we used a range() as the iterable
#lists are also iterables so we can naturally iterate over them 

#here we iterate over the elements in the list 'data" printing each one of them
print("\n\n............. using for loop to iterate over a list's elements")
data = [0.5, 0.6, 0.7, 1.2, 3.5, "hello", 4]

for el in data:
    print(el)


#if we want to know the index of each element as we iterate we can use the enumerate function
#this returns a pair of the index and the element value at that index at each step
print("\n\n............. using for loop to iterate over enumerate(list) getting the index and value of each element")
for i, el in enumerate(data):
    print(f'{i}th element is {el}')

#the above is equivalent to this slightly more verbose code
print("\n\n............. alternative iteration over list using index numbers")
for i in range(len(data)):
    print(f'{i}th element is {data[i]}')

#we can use this in order to modify a list by replacing each element with a new value
print("\n\n............. modifying elements of a list as we iterate through it")
print(f'list BEFORE loop is {data}')
for i, el in enumerate(data):
    data[i] = el*2
print(f'list AFTER loop is {data}')

#we can build a list from selected element from another list using a loop and a conditional statement
#here we filter all the elements in l1 that are greater than 2
print("\n\n............. create a list by selecting elements form another list")
l1 = [1, 5, 7, 3,6,2,2,4,0,7,3,5,7,2,7,8]
l2 = []
for el in l1:
    if el>2:
        l2.append(el)
print(f'l1 is {l1}')
print(f'l2 is {l2}')


#https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
#Because modifying each element of a list to build a new list is such a common task python has a shorthand
#for writing this sort of code called "comprehension" 
#this is done with a special syntax using a for loop enclosed in [] that generates a list as its output
#for example looping through each element and multiplying by two could be written like this
print("\n\n............. create a list from another list using the comprehension syntax")
data =[1 ,4, 5, 6, 7, 2,6, 8, 0]
data2 = [el*2 for el in data]
print(f'data is {data}')
print(f'data2 is {data2}')