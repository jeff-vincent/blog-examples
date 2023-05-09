import os

# looping through items in a list
list_items = ['apple', 'orange', 'pear']

def print_list_items(list_items):
    for item in list_items:
        print(item)

# looping through fields in a dictionary

dictionary = {'field1': 'value1', 'field2': 'value2', 'field3': 'value3'}

def print_dict_fields(dictionary):
    for key, value in dictionary.items():
        print(key, value)

# looping through all the files in the directory; 
# print files with .py extension

def get_py_files(directory=None):
    if directory:
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                print(filename)
    else:
        print("No directory specified")  # if directory is None

# for each item in list_items, print the item and 
# print the field in dictionary that corrosponds to 
# the item's index in the list

def nested_for_loops():
    for item in list_items:
        for field in dictionary:
            print(item, field)


if __name__ == "__main__":
    print('*** printing list items ***')
    print_list_items(list_items)
    print('*** printing dictionary fields ***')
    print_dict_fields(dictionary)
    print('*** printing .py files without passing a directory ***')
    get_py_files()
    print('*** printing .py files passing a directory ***')
    get_py_files(os.getcwd())
    print('*** printing nested for loops ***')
    nested_for_loops()