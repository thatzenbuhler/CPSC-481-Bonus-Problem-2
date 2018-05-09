# CPSC 481 Bonus Assignment Problem 2
# Perceptron Learning Algorithm example

# Given dataset for problem: x1, x2, output t
dataset = [ [1.0, 1.0, 1],
            [9.4, 6.4, -1],
            [2.5, 2.1, 1],
            [8.0, 7.7, -1],
            [0.5, 2.2, 1],
            [7.9, 8.4, -1],
            [7.0, 7.0, -1],
            [2.8, 0.8, 1],
            [1.2, 3.0, 1],
            [7.8, 6.1, -1] ]

# Arbitrary initial weights for algorithm
weights = [-0.2, 0.2]

def predict(row, weights):
    net = 0
    for i in range(len(row)-1):
       net += weights[i] * row[i]
    return 1.0 if net >= 0.0 else -1.0

for row in dataset:
    prediction = predict(row, weights)
    print("Expected = %d, Predicted = %d" % (row[-1], prediction))
