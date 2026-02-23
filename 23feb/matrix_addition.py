# Matrix Addition (Safe Version)

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []
result = []

print("\nEnter elements for Matrix 1:")
for i in range(rows):
    while True:
        row = list(map(int, input().split()))
        if len(row) == cols:
            matrix1.append(row)
            break
        else:
            print("Please enter exactly", cols, "values")

print("\nEnter elements for Matrix 2:")
for i in range(rows):
    while True:
        row = list(map(int, input().split()))
        if len(row) == cols:
            matrix2.append(row)
            break
        else:
            print("Please enter exactly", cols, "values")

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("\nResult Matrix:")
for row in result:
    print(row)