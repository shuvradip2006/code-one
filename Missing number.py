# Ask the user to input numbers separated by spaces
user_input = input("Enter numbers separated by spaces (e.g., 1 2 4 5): ")

# Convert input string to a list of integers
nums = list(map(int, user_input.strip().split()))

# Calculate the expected sum of numbers from 1 to n (where n = len(nums) + 1)
n = len(nums) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

# Find the missing number
missing = expected_sum - actual_sum
print(f"The missing number is: {missing}")