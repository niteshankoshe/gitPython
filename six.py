test_string = "Today is Friday"
for i in test_string:
    print(i)

test_string = "Best things in life are free"
print("free" in test_string)
print("free" not in test_string)

if "free" in test_string:
    print("Yes its present")

if "expensive" not in test_string:
    print("No its not present in string")