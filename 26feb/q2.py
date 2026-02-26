# Function to calculate sum of cubes

def sum_of_cubes(n):
    total = 0

    for i in range(1, n):
        total += i ** 3

    return total



num = int(input("Enter a positive integer: "))
print("Sum of cubes:", sum_of_cubes(num))