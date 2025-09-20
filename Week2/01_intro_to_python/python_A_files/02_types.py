#although python is not a strongly typed language, all variables ultimately store some
#value internally that is of a specific type. A type can be a number, string {text} or a more complex
#object such as an image or a file


#the type of the variable is determined by what you have assigned to it
a = 5               #int  stands for 'integer number'
b = 0.5             #float stands for 'floating point number' that is a representation of a real number
c = "hello"         #str stands for 'string' (of characters) that is text
d = [1,5]           #list

#each variable has a property __class__ that you can use to check its internal type
#we will almost never use this but its here for demonstration purposes
print("\n\n............. Type of variable")
print(a.__class__)

#the type of a variable changes if you assign a new value to it
print("\n\n............. Type of variable changed")
a = "some text"
print(a.__class__)

#because python does not know in advance what each variable type will be
#it allows you to write code that may break your program
#the following line would cause an error because a is a string and therefore
#there is no way to subtract a number from a piece of text. The 'text - number' operation is not defined
#b = a - 10


