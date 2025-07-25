#print  number from 1 to 100, for multiple of 3 print Fizz and for multiple of 5 print
#FizzBuzz
print_number = 1
while(print_number <= 100):
    if(print_number % 3 == 0 and print_number % 5 == 0):
        print("FizzBuzz")
    elif(print_number % 3 == 0):
        print("Fizz")
    elif(print_number % 5 == 0):
        print("Buzz")
    else:
        print(print_number)
    print_number += 1