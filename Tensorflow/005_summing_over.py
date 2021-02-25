from tensorflow import ones, reduce_sum, constant
import numpy as np
"""
https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=4
"""

# define a 2X3X4 tensor of ones
A = ones([2,3,4])
print(A.numpy())

#sum over all dimensions
B = reduce_sum(A)
print("reduce", B.numpy())

#Sum over dimension 0, 1 and 2
B0 = reduce_sum(A, 0)
print("-" * 10, "reduce 0", B0.numpy())

B1 = reduce_sum(A, 1)
print("-" * 10, "reduce 1", B1.numpy())

B2 = reduce_sum(A, 2)
print("-" * 10, "reduce 2", B2.numpy())


wealth_array = np.array([[11, 50],
       [ 7,  2],
       [ 4, 60],
       [ 3,  0],
       [25, 10]])

wealth = constant(wealth_array)

print('\n wealth: \n{}'.format(wealth.numpy()))    

print('\n reduzido pela coluna: \n{}'.format(reduce_sum(wealth, 0).numpy()))  
print('\n reduzido pela linha: \n{}'.format(reduce_sum(wealth, 1).numpy()))  