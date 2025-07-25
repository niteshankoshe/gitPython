#Palindrome string
#Return True or False
input_string = input("Enter the String\n")
reverse_string = ""
i = len(input_string)
while i > 0:
    i -= 1
    reverse_string = reverse_string + input_string[i]

print("your input String: ",input_string)
print("Palindrome String:", reverse_string)

if(input_string == reverse_string):
    print("True")
else:
    print("False")