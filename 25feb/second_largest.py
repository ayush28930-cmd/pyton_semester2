# Second Largest Number

lst = list(map(int, input("Enter list elements: ").split()))

largest = second = float('-inf')

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("No second largest number")
else:
    print("Second Largest:", second)