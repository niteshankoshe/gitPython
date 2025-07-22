#conditions
user_number = int(input("enter the number:"))
if(user_number % 2 == 0):
    print("Even Number")
else:
    print("Odd number")

#elif
const_number = 50
input_number = int(input("Enter the input number\n"))
input_number1 = int(input("Another number choice\n"))
input_number2 = int(input("Enter last choice:\n"))
if(const_number == input_number):
    print("you got the match first time")
elif(const_number == input_number1):
    print("Second matched")
elif(const_number == input_number2):
    print("Last choice is matched")
else:
    print("Try Later!!")

