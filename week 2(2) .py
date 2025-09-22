# Upper half
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()

# Lower half
for i in range(4, 0, -1):
    print(" " * (5 - i), end="")
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()