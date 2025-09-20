#A loop is a block of statements that gets repeated zero or more times
#it is one of the most fundamental building blocks for any algorithm
#in python most loops are defined using the syntax  
#for iterator in iterable: 
#the iterable is something that defines a sequence of things, like a range of numbers or a list of words
#the loop will repeat as many times as there are elements in the iterable
#the iterator is a variable that will be assigned each value of the iterable at each step of the loop

#print the number 0 to 9
#here we are using the range iterable that describes a sequence of numbers.
#this is equivalent to saying repeat 10 times...
print("\n\n............. loop N times using range(N)")
for i in range(10):
    print(i)

#a range does not have to start at 0
print("\n\n............. loop starting at A and  ending before B using range(A,B)")
for i in range(-3, 5):
    print(i)

#we can use a for loop to compute a sum for example
print("\n\n............. compute a sum total incrementally using a loop and a range")
total = 0
for i in range(1, 11):
    total += i*2
    print(f'step {i} : total = {total}')


#although for many of these simple operations python provides shortcuts
#the sum function will automatically add together the elements of any iterable
print("\n\n............. compute a sum total using the sum() function")
total = sum(range(1,11))
print(f'total using sum is {total}')