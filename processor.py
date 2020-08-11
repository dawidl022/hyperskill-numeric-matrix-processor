from determinant import determinant_calculator
def make_int(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            error()


def error():
    print("The operation cannot be performed.\n")
    menu()


def print_result_matrix(result_matrix):
    print("The result is:")
    for row in result_matrix:
        print(*row)
    print()


def input_matrix():
    global matrix1, m1, n1
    n1, m1 = input("Enter size of matrix: ").split()
    matrix1 = []
    print("Enter matrix:")
    for row in range(int(n1)):
        row_val = list(map(make_int, input().split()))
        if len(row_val) < int(m1):
            error()
        matrix1.append(row_val)


def input_2_matrices():
    global matrix1, matrix2, m1, m2, n1, n2
    n1, m1 = input("Enter size of first matrix: ").split()
    matrix1 = []
    print("Enter first matrix:")
    for row in range(int(n1)):
        row_val = list(map(make_int, input().split()))
        if len(row_val) < int(m1):
            error()
        matrix1.append(row_val)

    try:
        n2, m2 = input("Enter size of second matrix: ").split()
    except:
        error()
    matrix2 = []
    print("Enter second matrix:")
    for row in range(int(n2)):
        row_val = list(map(make_int, input().split()))
        if len(row_val) < int(m2):
            error()
        matrix2.append(row_val)


def scale_matrix():
    input_matrix()
    scaler = int(input("Enter constant: "))
    
    matrix_res = []
    for row in matrix1:
        res_row = list(map(lambda x: x * scaler, row))
        matrix_res.append(res_row)
    print_result_matrix(matrix_res)


def add_matrices():
    input_2_matrices()
    
    if m1 == m2 and n1 == n2:
        matrix_res = []
        for n, row in enumerate(matrix1):
            res_row = list(map(lambda x, y: x + y, row, matrix2[n]))
            matrix_res.append(res_row)
        print_result_matrix(matrix_res)

    else:
        error()


def main_transpose(matrix, m, side_diag=False, vertical=False, horizontal=False):
    matrix_transposed = []
    if vertical:
        for column in matrix:
            column.reverse()
            matrix_transposed.append(column)
    elif horizontal:
        matrix.reverse()
        return matrix
    else:
        for column in range(int(m)):
            matrix_columns = []
            for row in matrix:
                matrix_columns.append(row[column])
            if side_diag:
                matrix_columns.reverse()
                matrix_transposed.append(matrix_columns)
            else:
                matrix_transposed.append(matrix_columns)
        if side_diag:
            matrix_transposed.reverse()

    return matrix_transposed


def transpose_matrix():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    option = input("Your choise: ")
    input_matrix()
    if option == "1":
        matrix_res = main_transpose(matrix1, m1)
    elif option == "2":
        matrix_res = main_transpose(matrix1, m1, side_diag=True)
    elif option == "3":
        matrix_res = main_transpose(matrix1, m1, vertical=True)
    elif option == "4":
        matrix_res = main_transpose(matrix1, m1, horizontal=True)
    print_result_matrix(matrix_res)


def multiply_matrices():
    input_2_matrices()

    matrix2_final = main_transpose(matrix2, m2)

    if m1 == n2:
        matrix_res = []
        print("The result is:")
        for row in matrix1:
            matrix_res_row = []
            for column in matrix2_final:
                dot_sum = 0
                for position, element in enumerate(column):
                    dot_sum += element * row[position]
                matrix_res_row.append(dot_sum)
            matrix_res.append(matrix_res_row)
        print_result_matrix(matrix_res)
    else:
        error()

def calc_determinant():
    pass

def matrix_determinant():
    input_matrix()
    print("The result is:")


def menu():
    while True:
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit""")
        option = input("Your choise: ")
        if option == "0":
            break
        elif option == "1":
            add_matrices()
        elif option == "2":
            scale_matrix()
        elif option == "3":
            multiply_matrices()
        elif option == "4":
            transpose_matrix()
        elif option == "5":
            input_matrix()
            determinant_calculator(matrix1)
            print()
menu()