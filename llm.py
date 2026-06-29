from sympy import MatrixSymbol, Identity, lambdify
import numpy as np


# 定义符号（使用具体整数维度，lambdify 不支持符号维度的 Identity）
n = 2
A = MatrixSymbol('A', n, n)
a = np.array([[1, 2], [3, 4]])
f = lambdify(A, A + Identity(n))
print(f(a))