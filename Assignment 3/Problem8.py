import numpy as np


def strassen_multiply(A, B):
    n = len(A)
    if n <= 4:
        return np.dot(A, B)

    # Divide matrices into submatrices
    a11, a12, a21, a22 = A[:n // 2, :n // 2], A[:n // 2, n // 2:], A[n // 2:, :n // 2], A[n // 2:, n // 2:]
    b11, b12, b21, b22 = B[:n // 2, :n // 2], B[:n // 2, n // 2:], B[n // 2:, :n // 2], B[n // 2:, n // 2:]

    # Recursive calls for P1 to P7
    p1 = strassen_multiply(a11 + a22, b11 + b22)
    p2 = strassen_multiply(a21 + a22, b11)
    p3 = strassen_multiply(a11, b12 - b22)
    p4 = strassen_multiply(a22, b21 - b11)
    p5 = strassen_multiply(a11 + a12, b22)
    p6 = strassen_multiply(a21 - a11, b11 + b12)
    p7 = strassen_multiply(a12 - a22, b21 + b22)

    # Compute resulting submatrices
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6

    # Combine submatrices to get the final result
    C = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return C


def input_matrix():
    n = int(input("Enter the size of the matrix (e.g., 2 for a 2x2 matrix): "))
    print(f"Enter values for the {n}x{n} matrix:")
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return np.array(matrix)


def display_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    # Prompt user for matrices
    print("Enter the first matrix:")
    A = input_matrix()

    print("\nEnter the second matrix:")
    B = input_matrix()

    # Check if matrices are compatible for multiplication
    if len(A) != len(B[0]):
        print(
            "\nError: Matrices cannot be multiplied. The number of columns in the first matrix must be equal to the "
            "number of rows in the second matrix.")
    else:
        # Perform multiplication using Strassen algorithm
        result = strassen_multiply(A, B)

        # Display result
        print("\nResultant Matrix:")
        display_matrix(result)
