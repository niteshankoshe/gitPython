input_string = input("Enter the string\n").replace(" ","").lower()
reverse_string = input_string[::-1]
print("The input String", input_string)
print("The reverse is", reverse_string)
if input_string == reverse_string:
    print("True")
else:
    print("False")