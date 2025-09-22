# Two sorted arrays
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8, 9]

# Merging manually
merged = []
i = j = 0

# Merge while both arrays have elements
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

# Append remaining elements
merged.extend(arr1[i:])
merged.extend(arr2[j:])

print("Merged sorted array:", merged)