import math
#a function is a parameterized set of instructions, that take zero or more inputs (the arguments)
#and generates an output (the return value)
#we already used a function when calling math.cos()
#print is also a function that takes an input an outputs its text representation to the console
print("\n\n............. compute a cosine calling the predefined function math.cos(a)")
a = math.cos(0.5)
print(a)  


#we can define our functions by using the syntax
#def functionName(arg1, arg2, ...., argN):
# here is a function that adds two numbers
print("\n\n............. define a function that adds two numbers")
def add(a,b):
    return a+b

#and here is how to use it:
print("\n\n............. adding two float numbers")
a = add(0.5, 4.2)
print(a)
print("\n\n............. adding two integer numbers")
b = add(3, 4)
print(b)
print("\n\n............. adding (concatenating) two strings")
c = add("hello", " again")
print(c)

#the line 'def add(a,b):' is called the signature of the function
#it defines the name and the number of arguments that the function will accept
#after the : we can nest (tabulate) one or more instructions that are executed each time the function is called
#if the function is expected to generate an output then we can set the output by using the return statement
#whatever we place after the return keyword becomes the result that the function generates

#here is a function that uses a conditional to compute the larger of two numbers
print("\n\n............. a function that computes the maximum of two values")
def max2(a,b):
    if a>b:
        return a
    else:
        return b

m = max2(4, 8)
print(m)


#here is the function that computes the largest of 3 numbers
print("\n\n............. a function that computes the maximum of three values using conditional branching")
def max3(a,b,c):
    if a>b and a>c:     #is a the largest
        return a        #a it is
    elif b>c:           #is b the largest (a has already been ruled out during the first check)
        return b        #b it is
    else:
        return c        #only option left is c

print(max3(2,5,8))

#because return actually terminates and exits the function we can simplify it to:
print("\n\n............. a function that computes the maximum of three values using simpler branching")
def max3b(a,b,c):
    if a>b and a>c:
        return a

    if b>c:
        return b
 
    return c

print(max3(2,5,8))

#functions can be composited so the max3(a,b,c) can be implemented in terms of max2(a,b)
print("\n\n............. a function that computes the maximum of three values using the max2(a,b) function twice")
def max3c(a,b,c):
    return max2(a, max2(b,c))
    
print(max3(2,5,8))