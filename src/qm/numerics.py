"""
Utilidades numéricas base para Semana 1.
"""
import numpy as np

def residuo(A: np.ndarray, lam: float, x: np.ndarray) -> float:
    """||Ax - lam x||_2"""
    return np.linalg.norm(A @ x - lam * x)

def ortonormalidad(X: np.ndarray) -> float:
    """Retorna ||X^T X - I||_F para medir desviación de la ortonormalidad."""
    n = X.shape[1]
    return np.linalg.norm(X.T @ X - np.eye(n), ord="fro")
