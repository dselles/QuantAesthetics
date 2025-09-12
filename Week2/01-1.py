import math # this is a library for math functions

# This is a comment
# math and variables
h = math.cos(math.pi)
print(h)

a = 5
b = a/3
print(a)
print(b)

# strings
text = "Hello World" # this is a string. You can use single or double quotes.
print(text)
new_text = text.upper()
print(new_text)
print(text.replace("World", "Everyone"))
loc = text.find("W") # finds the first occurance from the start. rfind finds from the end.
print(loc)

# lists (sequences of values)
l = [0.5, 2.4, 3.6, 4.0, 6.0, 7.4] # lists are like arrays
print(l[0]) # grab the first element
print(l[-1]) # grab the last element
l.append(5.0) # add an element to the end of the list
print(l)
l.remove(2.4) # remove an element from the list
print(l)
print(len(l)) # length of the list
print(sum(l)) # sum of the list
print(min(l)) # minimum value in the list
print(max(l)) # maximum value in the list
l[2] = 10.0 # change the value of an element
print(l)
sub_list = l[1:4] # grab a sublist (from index 1 to index 3 (4 is not included ))
print(sub_list)
l.sort() # sort the list
print(l)