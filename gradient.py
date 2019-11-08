class GradientDescent:
    def __init__(self):


    def fit(self, train_x, train_y):
        # train_x is a list of lists
        # train_y is a panda Series

        # Initialize the weights to be len(train_x[0]) + 1
        number_of_features = len(train_x[0])
        number_of_weights = number_of_features + 1
        a = 0.1                             # learning rate
        weights = []
        for weight in range(number_of_weights):
            weights[weight] = 0.1
        print("weights are: {0}".format(weights))

        for number, instance in enumerate(train_x):
            # looping though each example of the training data
            instance.insert(0, 1)

            # use the formula: y = b0x0 + b1x1 ... bnxn
            predicted = 0                           # this is also the predicted

            for index in range(number_of_features):
                value = weights[index] * instance[index]
                predicted =+ value

            # Have y at this point, therefore get error (y-f(x))
            actual = train_y[number]        # this is the actual value for that instance obtained from the tain_y

            error = actual - predicted
            print("Error for this example is: {0}".format(error))

            # Use Widrow Hoff rule to update weight
            # new_weight = current_weight + leaning_rate(actual - predicted) * training_example x
            weights_new = []
            for i in range(len(weights)):
                new_weight = weights[1] + a * error * instance[i]
                weights_new[i] = new_weight

            # Need to check which weights have smallest error, and save that.



        print("fit")

    def predict(self, test_x):
        # test_x is a list of lists
        # returns y_pred which is a list
        print("predict")
