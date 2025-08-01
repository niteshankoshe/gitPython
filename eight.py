this_list = ["apple","orange","banana"]
print(this_list)
new_list = ["pinaple","watermelon","blueberries"]
this_list.extend(new_list)
print(this_list)
for x in this_list:
    print(x)


#get fruits with a in name
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []
for x in fruits:
    if 'a' in x:
        new_list.append(x)
print(new_list)

new_list1 = [x for x in fruits if 'a' in x]
print(new_list1)
