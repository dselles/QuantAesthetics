#conditional statements are code structure that enable branching in our code
#that is the program can take a different execution path depending on some
#test.
#the simplest conditional is an if statement that checks whether some condition is true and only then
#executes the lines of code nested below it
#in python this code 'nesting' is determined by tabs

print("\n\n............. Simple conditional statement")
a = 2
b = 5

if a<-5 :
    print('a is less than -5')

#the < operator results in a boolean True/False value
result = a<-5
print(result)
if result:
    print('a is less than -5')

print("\n\n............. Simple conditional statement with multiple lines of code")
if a<b:
    print('a is greater than b')
print('another line of code')
    
#conditional statements can define a block of code for each possible true/false outcome using the if/else structure
print("\n\n............. if/else branching")
if a<b:
    print('a is less than b')
else:
    print('a was is not than b')

#you can chan multiple of these conditions using the elif statement
print("\n\n............. if/elif/else chained branching")
if a<b:
    print("branch a<b")
elif a==b:
    print("branch a==b")
else:
    print("branch a>b")


#the condition in a conditional statement can be a logical combination of other conditions using the 'or', 'and', 'not' keywords
print("\n\n............. logical operators in conditional test")
a = 3
if a<5 and a>0:
    print('a is between 0 and 5')

if a>15 or a<-6:
    print('a is outside the [-6,15] range')

