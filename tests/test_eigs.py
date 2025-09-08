import numpy as np
from src.qm.numerics import residuo, ortonormalidad

def test_identity_has_zero_residual():
    A = np.eye(3)
    vals, vecs = np.linalg.eig(A)
    # Para identidad, todos los autovalores son 1 y los autovectores forman base
    res_max = max(residuo(A, lam, vecs[:, i]) for i, lam in enumerate(vals))
    assert res_max < 1e-12

def test_orthonormality_close():
    # Matriz simétrica bien condicionada
    rng = np.random.default_rng(123)
    M = rng.standard_normal((3,3))
    A = (M + M.T)/2
    vals, vecs = np.linalg.eigh(A)
    err_ortho = ortonormalidad(vecs)
    assert err_ortho < 1e-12
