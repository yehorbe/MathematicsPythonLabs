import numpy as np
import matplotlib.pyplot as plt

def problem1(id):


    rng = np.random.default_rng(id)
    A = rng.integers(low=1, high=10, size=(5, 5))
    while np.linalg.det(A) == 0:  
        A = rng.integers(low=0, high=10, size=(5, 5))
    A = A/np.linalg.norm(A)
    B = np.zeros_like(A, dtype=float)
    n = A.shape[0]
    I = np.eye(n)
    C = np.hstack((A, I))
    for i in range(n):
        C[i] = C[i] / C[i, i]
        for j in range(n):
            if i != j:
                C[j] = C[j] - C[i] * C[j, i]
    B = C[:, n:]
    return A, B

def problem2(id):

    rng = np.random.default_rng(id)
    A = rng.integers(low=-10, high=10, size=(3, 3))
    b = rng.integers(low=-10, high=10, size=(3, 1))
    return A, b

def problem3(id):
    rng = np.random.default_rng(id)
    n = len(str(id))
    A = np.round(rng.uniform(-1000, 1000, size=(n, n)), 4)
    b = A @ np.array([int(d) for d in str(id)]).reshape((n, 1))
    return A, b
