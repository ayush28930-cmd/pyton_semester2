# Remove Duplicates

lst = list(map(int, input("Enter list elements: ").split()))

unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("List without duplicates:", unique)