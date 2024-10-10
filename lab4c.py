#!/usr/bin/env python3

# Function to create a dictionary from two lists
def create_dictionary(keys, values):
    i = 0
    result = {}
    while i < len(keys):
        result[keys[i]] = values[i]
        i += 1
    return result

# Function to find shared values between two dictionaries
def shared_values(dict1, dict2):
    return set(dict1.values()) & set(dict2.values())

if __name__ == '__main__':
    # Initialize the lists and dictionaries
    list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
    list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

    dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
    dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}

    # Create the dictionary from lists
    york = create_dictionary(list_keys, list_values)
    print(york)
    common = shared_values(dict_york, dict_newnham)
    print(common)
