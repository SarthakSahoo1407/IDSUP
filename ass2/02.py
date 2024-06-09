def create_sum_matrix(order):
    matrix = []
    for i in range(order):
        row = []
        for j in range(order):
            row.append(i + j)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    order = int(input("Enter the order of the matrix: "))
    if order <= 0:
        print("Order should be a positive integer.")
        return

    result_matrix = create_sum_matrix(order)
    print("\nThe matrix with (i,j)th entry as the sum of i and j:")
    print_matrix(result_matrix)

if __name__ == "__main__":
    main()
