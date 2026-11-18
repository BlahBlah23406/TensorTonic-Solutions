import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A)
    N, M = A.shape
    out = np.zeros((M, N), dtype=A.dtype)

    for i in range(N):
        for j in range(M):
            out[j, i] = A[i, j]

    return out
    
    pass
