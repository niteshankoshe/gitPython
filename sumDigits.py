input_number = int(input("Enter the number:\n"))
def sum_of_digit(num)-> int:
    number_added = 0
    while num >= 10:
        reminder = num % 10
        num = int(num / 10)
        number_added = number_added + reminder
    if num < 10:
        number_added = number_added + num
    return number_added

print_number = sum_of_digit(input_number)
print("The sum of Digit is",print_number)
