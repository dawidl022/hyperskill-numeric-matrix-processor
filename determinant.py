from copy import deepcopy
#debugging examples
matrix0 = [[2, 0, 4], [1, 2, 4], [4, 4, 2]]
matrix1 = [[1, 7, 7], [6, 6, 4], [4, 2, 1]]
matrix3 = [[1, 2, 3, 4, 5], [4, 5, 6, 4, 3], [0, 0, 0, 1, 5], [1, 3, 9, 8, 7], [5, 8, 4, 7, 11]]
matrix2 = [[45, 2, 11, 5], [0, 0, 0, -4], [7, -2, 3, 2], [-4, 1, 0, 8]]
matrices = []
determinant = 0
calculations = 0

def store_matrix(minor_matrix, cofactor):
    matrices.append((minor_matrix, cofactor))

def retrieve_matrix():
    for count, matrix in enumerate(matrices):
        if len(matrix[0]) == 2:
            matrices.pop(count)
            calc_determinant(matrix[0], matrix[1])
        else:
            matrices.pop(count)
            calc_matrix(matrix[0], matrix[1])

def calc_determinant(matrix, cofactor=1):
    global determinant, calculations
    determinant += cofactor * (matrix[0][0] * matrix [1][1] - matrix [0][1] * matrix[1][0])
    calculations += 1

def calc_matrix(matrix, cofactor=1):
    if len(matrix) == 2:
        calc_determinant(matrix, cofactor)
    global cofactors
    orig_matrix = deepcopy(matrix)
    orig_cofactor = deepcopy(cofactor)
    for count, row in enumerate(matrix):
        minor_matrix = deepcopy(orig_matrix)
        new_cof = minor_matrix.pop(0)[count]
        cofactor = new_cof * orig_cofactor
        for column in minor_matrix:
            column.pop(count)
        store_matrix(minor_matrix, cofactor * (-1) ** count)
    retrieve_matrix()

def init_matrix(matrix, cofactor=1):
    if len(matrix) == 2:
        calc_determinant(matrix)
    global cofactors
    orig_matrix = deepcopy(matrix)
    for count, row in enumerate(matrix):
        minor_matrix = deepcopy(orig_matrix)
        cofactor = minor_matrix.pop(0)[count]
        for column in minor_matrix:
            column.pop(count)
        store_matrix(minor_matrix, cofactor * (-1) ** count)
    retrieve_matrix()

def determinant_calculator(matrix):
    print("The result is:")
    if len(matrix) == 1:
        print(matrix[0][0])
    else:
        init_matrix(matrix)
        while len(matrices) > 0:
            retrieve_matrix()
        print(determinant)
