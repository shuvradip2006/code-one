# Original list with some empty strings
string_list = ["apple", "", "banana", "", "cherry", ""]

# Remove empty strings
filtered_list = [s for s in string_list if s]

print(filtered_list)