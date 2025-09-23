# Original list
fruits = ["apple", "banana", "cherry"]

# Item to insert and the reference item
new_item = "orange"
after_item = "banana"

# Insert new_item after after_item
if after_item in fruits:
    index = fruits.index(after_item)
    fruits.insert(index + 1, new_item)

print(fruits)