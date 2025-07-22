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

#Matched
input_number3 = int(input("Enter number between 1 to 5\n"))
match input_number3:
    case 1: print("Your number is 1")
    case 2: print("your number is 2")
    case 3|4: print("your number is 3 or 4")
    case 5: print("your number is 5")
    case _: print("you entered someting out of range")

