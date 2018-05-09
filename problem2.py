# CPSC 481 Bonus Assignment Problem 2
# Perceptron Learning Algorithm example
# Tyler Hatzenbuhler
# Anette Ulrichsen
# Team THAU

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

# Arbitrary initial weights for algorithm for x1, x2, and bias
weights = [-0.2, 0.2, 1]

#Calculates f(net) for current row to determine if weights match
def predict(row, weights):
    net = 0
    for i in range(len(row)-1):
       net += weights[i] * row[i]
    net += weights[-1] * 1.0 # Bias weight
    return 1.0 if net >= 0.0 else -1.0

finished = False
learnrate = 0.2
epoch = 1

# Main loop that iterates through dataset until correct weights are found
while finished == False:
    print("\nEpoch %d" % (epoch))
    epoch += 1
    finished = True # Switches to false if a change occurs
    for index, row in enumerate(dataset):
        prediction = predict(row, weights)
        if prediction == row[-1]:
            continue
        else:
            deltaWeight = learnrate * (row[-1] - prediction)
            for i in range(len(row)-1):
                weights[i] = weights[i] + (deltaWeight * row[i])
            weights[-1] += deltaWeight * 1.0 # Bias weight
            print("Row %d doesn't match, Weight adjusted by %f" % (index, deltaWeight))
            print("New weight vector: ", weights)
            finished = False
    if finished == True: print("All rows match weight vector.")

print("\nTraining complete! It took %d epochs." % (epoch - 1))
print("Final weight vector: ", weights)

