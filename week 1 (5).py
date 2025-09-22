# Original array with duplicates
arr = [10, 20, 10, 30, 40, 20, 50, 30]

# Remove duplicates while preserving order
unique_arr = []
for item in arr:
    if item not in unique_arr:
        unique_arr.append(item)

print("Array after removing duplicates:", unique_arr)