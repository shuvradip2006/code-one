# Sample array
arr = [15, 3, 9, 27, 6, 18]

# Initialize max and min with the first element
max_val = min_val = arr[0]

# Traverse the array
for num in arr[1:]:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

# Display results
print("Maximum element:", max_val)
print("Minimum element:", min_val)