#https://docs.python.org/3/tutorial/

#all lines that start with # are comments and ignored by python

#you can declare a variable by simply assigning a value to a token of your choice

#declare a variable called 'a' with initial value of 5
#notice the assignment operator "=" DOES NOT define an equation 
#it simply assigns a value computed on the right side to the variable on its left side
#think of 'a = 5' as 'store the value 5 in a' or 'set a to the value 5'
print("\n\n............. Variable declaration")
a = 5

#you can read and print the value of 'a' at any point
print(a) 

#you can change the value of the variable at any point by assigning a new value
print("\n\n............. Variable value assignment")
a = 6
print(a)

#you can assign values to variables computed from other variables
print("\n\n............. Variable value computed")
b = a*10
print(b)

#for numerical variables normal arithmetic operations work as expected
print("\n\n............. Basic arithmetic")
c = a + 5
d = a*2 + 5*(b-1)
print(c)
print(d)


