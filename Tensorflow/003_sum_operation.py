from tensorflow import constant, add
"""
https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=4
"""

#Define 0-dimensional tensors
a0 = constant([1])
b0 = constant([2])

#Define 1-dimensional tensors
a1 = constant([1, 2])
b1 = constant([3, 4])

#Define 3-dimensional tensors
a2 = constant([[1, 2], [3, 4]])
b2 = constant([[5, 6], [7, 8]])

c0 = add(a0, b0)
c1 = add(a1, b1)
c2 = add(a2, b2)

print('c0', c0.numpy())
print('=' * 30)
print('c1', c1.numpy())
print('=' * 30)
print('c2', c2.numpy())