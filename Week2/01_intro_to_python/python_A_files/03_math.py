#use import to reference libraries that add functionality to your code
#math for example contains all the regular mathematical functions like sines, cosines etc...
import math

#you can access the functions contained in the math library (python module)
#by using the dot notation. The dot in general allows you to access properties of things 
#or functions that are defined in some module you imported or for some type of object
#the parentheses following the cos function cause an evaluation to happen (a function call)
#where 0.5 is called the argument and the result (the returned value) is stored in the variable 'a'
print("\n\n............. using the math module's functions")
a = math.cos(0.5)
b = a*math.exp(-10.0) + 0.7
c = max(a,b)

print(a)
print(b)
print(c)