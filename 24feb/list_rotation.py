# List Rotation

lst = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter rotation count: "))

k = k % len(lst)  # Handle large k

rotated = lst[-k:] + lst[:-k]

print("Rotated List:", rotated)