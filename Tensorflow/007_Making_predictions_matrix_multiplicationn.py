from tensorflow import ones, constant, multiply, matmul, ones_like
"""
https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=6
                     
"""

# Define features, params, and bill as constants
features = constant([[2, 24], [2, 26], [2, 57], [1, 37]])
params = constant([[1000], [150]])
bill = constant([[3913], [2682], [8617], [64400]])

# Compute billpred using features and params
billpred = matmul(features, params)
print('\n billpred: {}'.format(billpred.numpy()))

# Compute and print the error
error = bill - billpred
print(error.numpy())

