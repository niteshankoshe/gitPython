#Global variable
x = "apple"
def fruits():
    print("Fruit is:",x)

fruits()

#Gloabl variable with same local variable name
y = "beer"

def drinks():
    y = "rum"
    print("Drinks:",y)

drinks()
print("Default Drink:",y)

#global keyword

def myFunction():
    global z
    z = "clean"

myFunction()
print("My activity:",z)