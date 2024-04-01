def append_dicts(dict1, dict2):
    dict1.update(dict2)

# Example dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

append_dicts(dict1, dict2)
print("Resulting dictionary after appending:")
print(dict1.values)