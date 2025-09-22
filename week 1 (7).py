def rotate_array(arr, k, direction='left'):
    n = len(arr)
    k = k % n  # Handle cases where k > n

    if direction == 'left':
        rotated = arr[k:] + arr[:k]
    elif direction == 'right':
        rotated = arr[-k:] + arr[:-k]
    else:
        raise ValueError("Direction must be 'left' or 'right'")

    return rotated

# Example usage
arr = [10, 20, 30, 40, 50]
k = 2

print("Original array:", arr)
print("Left rotation by", k, ":", rotate_array(arr, k, 'left'))
print("Right rotation by", k, ":", rotate_array(arr, k, 'right'))