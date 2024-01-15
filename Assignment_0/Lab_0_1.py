# 1. Write a program to read a matrix of any order and enter the values into the matric through the keyboard. Read the rows, cols, enter and print the matrix.

# Entering the matrix
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

matrix = input_matrix(row, col, "Matrix")
print_matrix(matrix, "Matrix")





