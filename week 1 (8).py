# Sample array
arr = [10, 20, 10, 30, 20, 40, 10]

# Dictionary to store frequencies
frequency = {}

# Count each element
for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

# Display frequencies
print("Element frequencies:")
for key, value in frequency.items():
    print(f"{key}: {value}")