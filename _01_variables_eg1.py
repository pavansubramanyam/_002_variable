#assiging a integer value to the variable
print("----Integer Number----")
x = 10
print("integer number is:",x)

#assiging the float value to the variable
print("----Floating Point Number----")
y = 20
print("Float value is:",y)

#assiging string to the variable
print("----string value----")
language = "Python"

#assiging the one value to multi variables
x = y = z = 10
print(x)
print(y)
print(z)
#another example multiple assignmnet
print("----multiple assignment---")
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)

#plus operation on the variables
print("----plus operation----")
a1 = 10
a2 = 20
a3 = a1 + a2
print("adding of a1, a2 is:",a3)

#creating a global varible
print("---global varible----")
x = "global"
def myfunc():
    print("x is inside function", x)

myfunc()
print("x is outside function", x)

#Create a variable inside a function,
# with the same name as the global variable
print("----creating a variable inside the function----")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#if you want to change a global variable inside a function
# we can use the global keyword
print("--changing global variable inside the function----")
x = "outside"
def my_func1():
    global x
    x = "inside"
my_func1()
print("variable is in:",x)


#without using global keyword for accessing the global variable
print("----without using global keyword----")
#global variables
a = 10
b = 20
#function to perform addition
def add():
    c = a + b
    print(c)
#calling the function
add()
print("----without using global keyword----")

#global string variables
fname = "siva"
sname = "keshav"
def name():
    fullname = fname + sname
    print("fullname is:",fullname)
name()
print("\n")
#using global keyword in Nested functions
# Python program showing a use of
# global in nested function
print("----using global function in nested function----")
print("\n")
def add1():
    x1 = 15

    def change():
        global x1
        x1 = 20

    print("Before making changing: ", x1)
    print("Making change")
    change()
    print("After making change: ", x1)


add1()
print("value of x1", x1)
