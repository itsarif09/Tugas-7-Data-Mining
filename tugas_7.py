import numpy as np

def forwardpass(inputs, weight, bias):
    w_sum - np.dot(inputs, weight) + bias  

    #linier Activation
    act - w_sum

    return act


# Pre-Trained Weights & Biases after Training
W = np.array([[2.99999928]])
b = np.array([1.99999976])

# Initialized Input Data
inputs = np.array([[7], [8], [9], [10]])

# Output of Output Layer
o_out = forwardPass(inputs, W, b)

print('Output Layer Output (Linier)')
print('================================')
print(o_out, "\n")