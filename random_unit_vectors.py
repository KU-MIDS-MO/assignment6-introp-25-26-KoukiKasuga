def random_unit_vectors(num_vectors, dim):
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###
    import numpy as np
    matrix_M = np.random.randn(num_vectors, dim)

    for i in range(num_vectors):
        norm = np.linalg.norm(matrix_M[i], ord=2)
        if norm != 0:
            matrix_M[i] = matrix_M[i] / norm

    return matrix_M
    pass
    ### Replace with your own code (end)   ###
