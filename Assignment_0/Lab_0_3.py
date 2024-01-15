# 3. Write a program to multiply two matrices
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of cols: "))

# Function for Entering Matrix
def input_matrix(row, col, name):
  print(f'---- Entering {name}: ----')
  matrix = []
  for i in range(row):
    rows = []
    for j in range(col):
      ele = int(input(f'Enter {i + 1} x {j + 1} element: '))
      rows.append(ele)
    matrix.append(rows)
  return matrix

# Function for printing Matrix
def print_matrix(matrix, name):
  print(f'---- Printing {name}: ----')
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix[i][j], " ", end=" ")
    print()

# Function for multiplying Matrix
def multiply_matrix(matrix1, matrix2):
  # Multiplying the Matrix
  multiply_matrix = []
  # Iterating the rows of matrix 1
  for i in range(len(matrix1)):
    rows = []
    # Iterate through columns of matrix 2
    for j in range(len(matrix2[0])):
      product = 0
      # Iterate through rows of matrix 2
      for v in range(len(matrix1[i])):
        product += matrix1[i][v] * matrix2[v][j]
      rows.append(product)
    multiply_matrix.append(rows)
  return multiply_matrix

# Entering both matrix
matrix1 = input_matrix(row, col, "Matrix 1")
matrix2 = input_matrix(col, row, "Matrix 2")

# Printing the Matrices
print_matrix(matrix1, "Matrix 1")
print_matrix(matrix2, "Matrix 2")

# Multiplication
result = multiply_matrix(matrix1, matrix2)

# Printing the result
print_matrix(result, "Result Multiplication Matrix")