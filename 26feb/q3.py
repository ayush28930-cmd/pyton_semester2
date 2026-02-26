# Recursive function to print 1 to n

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)



num = int(input("Enter a number: "))
print_numbers(num)