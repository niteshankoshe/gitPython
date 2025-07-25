input_number = int(input("Enter the number:\n"))
digit = 0
while input_number > 0:
    input_number = abs(input_number)
    digit += input_number % 10
    input_number //= 10

print(digit)
