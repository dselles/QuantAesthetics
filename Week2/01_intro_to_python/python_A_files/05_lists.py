#https://docs.python.org/3/tutorial/introduction.html#lists

#there are several structures in python that allow us to store sets of data
#the most common one is the list which stores a sequence of things
#you can define a list using the square brackets [] 

#a is an empty list
print("\n\n............. creating an empty list")
a = []
print(a.__class__)

#or you can give it some initial values right away
print("\n\n............. creating a list with initial values")
a = [2, 5, -1, 7, 90]
print(a)

#in python lists can be heterogeneous. That is they can contain 
#data of different types
print("\n\n............. creating a list with heterogeneous initial values")
h = [2, 0.5, 3.5, "hello",3, "again"]
print(h)

#you can also have lists of lists
h = [[2, 3], [-2, 4], [1, 3]]
print(h)

#you can read and write individual elements form a list using the square brackets as a subscript
#indexing for lists is zero based, so the first elements is [0]
print("\n\n............. reading an element from a list")
print(h[2])

#we can overwrite an element in a list
print("\n\n............. overwriting an element in a list")
h[3] = 12344
print(h)

#you can also access element in reverse with [-1] being the last element in the list
print("\n\n............. reading an element from a list, indexing starting at end")
print(h[-2])

#if you have a variable that holds a list you can find out how many elements it contains using the len() function
print("\n\n............. get the number of elements in a list")
print(len(h))

#you can also extract sublist of a list using slices [:]
print("\n\n............. extracting a sublist portion from a list (slicing)")
a = [0, 1, 2, 3, 4, 5, 6]
#get elements from position 2 (3rd element) to end
print(a[2:])

#get elements between positions 2 and 5
print(a[2:5])

#get the last 2 elements
print(a[-2:])


#lists can grow using the append() method to add an element at the end of the list
print("\n\n............. add elements to list using list.append(element)")
a = ["red", "green"]
print(a)
a.append("blue")
print(a)

#you can also delete elements from a list using the remove statement
#this will remove the first element found that matches the argument
print("\n\n............. remove an element from list given its value, list.remove(element)")
a.remove("green")
print(a)

#or delete an element at a specific location using the del() functions
print("\n\n............. remove an element from list given its index, del(list[index])")
del(a[0])
print(a)

#a useful method is the ability to sort a list
print("\n\n............. sort the values in a list in ascending order")
a = [0.5, -0.1, 2.3, 3.5, 4.8]
a.sort()
print(f'sorted a is {a}')

#a string is also a list of characters and supports some of the same functions
print("\n\n............. strings can be accessed as lists")
b = "hello hello"
print(b[0])
print(b[-2])
print(b[3:7])
print(len(b))

print("\n\n............. more types of containers")
#there are three more containers often used in python, the tuple, the dictionary and the set

#a tuple is like a list but after you create it you can change it in anyway (overwrite or add/remove elements)
#it is what we call an "immutable" container. It is initialized using () enclosing the list of elements instead of []
print("\n\n............. tuples are immutable lists")
a =(1, "hello")
print(a)
#a[0] = 5  #This will throw an error

#a set is a collection of unique items and is initialized by using curly braces {}
#it will coalesce all repeating elements. Also for sets the order is not guaranteed
print("\n\n............. sets are containers that only store unique items (no duplicates)")
a = {"hello", 1, 2, 4, 5, 4, 8, "hello"}
a.add(5) #it will have no effect 5 already exists
a.add(1000) #ok 
print(f'set a is {a}')


#finally the dictionary is a collection that allows you to look up a value from an associated key
#very often the key is a string
#you can create a dictionary with the curly braces {} and a series of key value pairs
#where the key and value are separated by :
print("\n\n............. dictionaries allow you to look up values given some associated keys")
a = {"red" : 0.4, "green": 100.0, "blue" : 3.4, "cyan" : 3}

#we can lookup a value in the dictionary using the [] 
b = a['green']
print(a)
print(f'green has the value {b}')