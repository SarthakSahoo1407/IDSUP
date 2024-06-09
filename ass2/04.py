def component_wise_mean(vectors):
    vector_length = len(vectors[0])
    assert all(len(vector) == vector_length for vector in vectors), "All vectors must be of the same length."
    mean_vector = []
    for i in range(vector_length):
        component_sum = sum(vector[i] for vector in vectors)
        mean_component = component_sum / len(vectors)
        mean_vector.append(mean_component)
    
    return mean_vector
vectors = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mean_vector = component_wise_mean(vectors)
print("Component-wise mean vector:", mean_vector)
