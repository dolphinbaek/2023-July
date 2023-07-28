#basics of python as taught by chatgpt

"""
() - used for tuples (tuh-ples) - are immutable . e.g. my_tuple = (1,2,3)
or used as function calls print("hello,wold")
or used for grouping expressions x = (2+3) - 4

[] - used for defining lists, they can change. e.g. 

my_list = [1,2,3]
my_list.append(5)
print(my_list)

or for accessing elemments from lists, tuples, and strings.

my_list = [1,2,3]
my_list.append(5)
print(my_list[1]) # note that the index starts at 0
print(my_list[3]) # result will be the 5 appended
print(my_list[4]) # result says IndexError: list index out of range

{} - used for dictionaries a.k.a unordered collection of key-value pairs and sets a.k.a unordered collection of unique elements,

# Dictionary
my_dict = {"name": "John", "age": 30}

# Set
my_set = {1, 2, 3, 4}

print(my_dict)
print(my_dict["name"])
"""


    

a = 5
b = 6
c = a + b
print(c)

age = 20

if a >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

