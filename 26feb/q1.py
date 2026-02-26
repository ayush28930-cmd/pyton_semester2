# Function to find max and min without using built-in functions

def find_max_min(numbers):
    if len(numbers) == 0:
        return "Empty list"

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum



nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = find_max_min(nums)

print("Maximum:", result[0])
print("Minimum:", result[1])