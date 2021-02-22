from tensorflow import ones, constant, multiply, matmul, ones_like
"""
https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=5
|1 2| x |3 1| = |3 2|                       
|2 1|   |2 5|   |4 5|                      
"""

# Define tensors A1 and A23 as constants
A1 = constant([1, 2, 3, 4])
A23 = constant([[1, 2, 3], [1, 6, 4]])
print('\n A1: {}'.format(A1.numpy()))
print('\n A23: {}'.format(A23.numpy()))

# Define B1 and B23 to have the correct shape
B1 = ones_like(A1)
B23 = ones_like(A23)
print('\n B1: {}'.format(B1.numpy()))
print('\n B23: {}'.format(B23.numpy()))


# Perform element-wise multiplication
C1 = multiply(A1, B1)
C23 = multiply(A23, B23)

# Print the tensors C1 and C23
print('\n C1: {}'.format(C1.numpy()))
print('\n C23: {}'.format(C23.numpy()))