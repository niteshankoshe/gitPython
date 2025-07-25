#function
def printFun():
    print("Print from the function")

printFun()

#calculate the number and return from the function
def summarize() -> int:
    sumUp = number1 + number2
    return sumUp

number1 = int(input("Enter the number 1\n"))
number2 = int(input("enter the second number\n"))
#sum_num = summarize()
print("total is", summarize())

#default argument
def printArguments(name, age):
    print("Name is", name)
    print("Age is", age)

printArguments("AC",20)