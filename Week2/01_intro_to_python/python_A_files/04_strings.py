#a string is a piece of text encoded as a sequence of characters
#you define a string by using single or double quotation marks
print("\n\n............. Declaring string variables")
a = 'hello'
b = "goodbye"
print(a)
print(b)

#you can join (concatenate) strings together to form larger strings
print("\n\n............. String concatenation")
c = a+b
print(c)

#or better
print("\n\n............. String better concatenation")
c = a + " " + b
print(c)

#strings have many useful methods you can access using the dot notation
print("\n\n............. string.capitalize() function ")
a = "hello"
a_caps = a.capitalize()
print(a_caps)
print("\n\n............. string.upper() function ")
print(a.upper())

#very useful for our purposes is the ability to split a string to substring at specific characters like spaces and commas
print("\n\n............. string.split() function ")
a = 'one two three four five six'
b = a.split(' ')
#b is now a structure called a list that contains many strings, one for each word in the original string
print(b)

#string interpolation is a handy syntax to easily build strings that contain values from variables
#you use an f in front of the quotation marks and include variables inside enclosed in curly braces{}
#which will get replaced by the values of the variables
print("\n\n............. String interpolation ")
a = 0.5
b = 2.3
c = f'a is equal to {a} and b is equal to {b}'
print(c)

#Be careful with the backslash. Traditionally it has been used to form what we call escape sequences
#that is combinations of characters that result in some non printable effect like "new line" or "tab"
#for example the combination \n stands for the new line character which is equivalent to pressing enter
print("\n\n............. String escape sequences pitfalls ")
print('yes\no')
#use two backslashes to negate the escape sequence
print('yes\\no')