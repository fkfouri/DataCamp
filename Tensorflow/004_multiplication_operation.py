from tensorflow import ones, constant, multiply, matmul
"""
https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=4
"""

#Define 0-dimensional tensors
a0 = constant([1])
b0 = constant([2])

#Define 1-dimensional tensors (vetor)
a1 = constant([1, 2])
b1 = constant([3, 4])

#Define 3-dimensional tensors (matriz) - mesmo numero de colunas e linhas
a2 = constant([[1, 2], [3, 4]])
b2 = constant([[5, 6], [7, 8]])

c0 = multiply(a0, b0)
c1 = multiply(a1, b1)
c2 = multiply(a2, b2)

print('c0', c0.numpy())
print('=' * 30)
print('c1', c1.numpy())
print('=' * 30)
print('c2', c2.numpy())


a0 = ones(1)

a31 = ones([3, 1])

a34 = ones([3, 4])
a43 = ones([4, 3])


print('===' * 30)
print(a0.numpy())
print(multiply(a0, a0).numpy())
print('===' * 30)
print(a31.numpy())
print(multiply(a31, a31).numpy())
print('===' * 30)
print(a34.numpy())
print(multiply(a34, a34).numpy())
print('===' * 30)
print(a43.numpy())
print(matmul(a43, a34).numpy())
