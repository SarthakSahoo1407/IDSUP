import math

def add_vectors(vector1, vector2):
    return [vector1[i] + vector2[i] for i in range(len(vector1))]

def subtract_vectors(vector1, vector2):
    return [vector1[i] - vector2[i] for i in range(len(vector1))]

def scalar_multiply(vector, scalar):
    return [scalar * element for element in vector]

def dot_product(vector1, vector2):
    return sum(vector1[i] * vector2[i] for i in range(len(vector1)))

def vector_length(vector):
    return math.sqrt(sum(element**2 for element in vector))

def main():
    while True:
        print("\nMenu:")
        print("1. Add vectors")
        print("2. Subtract vectors")
        print("3. Scalar multiplication")
        print("4. Dot product")
        print("5. Length of a vector")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vector1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(',')))
            vector2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(',')))
            print("Result:", add_vectors(vector1, vector2))

        elif choice == '2':
            vector1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(',')))
            vector2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(',')))
            print("Result:", subtract_vectors(vector1, vector2))

        elif choice == '3':
            vector = list(map(float, input("Enter vector (comma-separated values): ").split(',')))
            scalar = float(input("Enter scalar: "))
            print("Result:", scalar_multiply(vector, scalar))

        elif choice == '4':
            vector1 = list(map(float, input("Enter vector 1 (comma-separated values): ").split(',')))
            vector2 = list(map(float, input("Enter vector 2 (comma-separated values): ").split(',')))
            print("Result:", dot_product(vector1, vector2))

        elif choice == '5':
            vector = list(map(float, input("Enter vector (comma-separated values): ").split(',')))
            print("Length of vector:", vector_length(vector))

        elif choice == '6':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
