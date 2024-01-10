my_dict = {'name': 'John', 'age': 30, 'address': '123 Street'}

print(my_dict.get('address',"Not Found"))
print(my_dict['address'])

length = len(my_dict)

#get list of key,values and items
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print()

# create a new dictionary
my_dict2 = dict(name='Sara', age=25)
print(my_dict2)

# add a default value if the item does not already exist
my_dict2.setdefault('address','new street')
print(my_dict2)

# remove a key-value pair from a dictionary. 
removed_value = my_dict.pop('address')
print(my_dict2)

#check if a key exists
print('name' in my_dict2)

#shallow copy of a dict
new_dict = my_dict2.copy()


my_dict3 = {'b': 2, 'a': 4, 'c': 3}
#sort dict by keys
# sorted_dict = dict(sorted(my_dict3.items()))
sorted_dict = dict(sorted(my_dict3.items(), key=lambda item: item[0]))
print(sorted_dict)

#sort dict by values
sorted = dict(sorted(my_dict3.items(), key=lambda item: item[1],reverse=True))
print(sorted)

#dictionary comprehension
squares = {key: value**2 for (key,value) in my_dict3.items()}
print(squares)

#return key for a value in dict
value = {i for i in my_dict3 if my_dict3[i]==4}
print("key by value:",value)

for key, value in my_dict3.items():
    if value == 2:
        print(key)