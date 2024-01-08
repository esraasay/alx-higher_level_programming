#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    # Validate m_a and m_b
    validate_matrix(m_a)
    validate_matrix(m_b)

    # Validate if m_a and m_b can be multiplied
    validate_multiplication(m_a, m_b)

    # Get the dimensions of the matrices
    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

def validate_matrix(matrix):
    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Check if matrix is not empty
    if not any(matrix):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if elements are integers or floats
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    # Check if the matrix is a rectangle
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

def validate_multiplication(m_a, m_b):
    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
