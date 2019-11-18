class GradientDescent:
    def __init__(self):
        self.min = None

    def __del__(self):
        self.min = None

    def check_lowest_error(self, error, weights):
        if not self.min:
            self.min = {
                "error": error,
                "weights": weights
            }
            print("Minimum error is now: {0} and using weights: {1}".format(self.min['error'], self.min['weights']))
        else:
            if abs(self.min['error']) > abs(error):
                self.min['error'] = error
                self.min['weights'] = weights
                print("Minimum error is now: {0} and using weights: {1}".format(self.min['error'], self.min['weights']))
            else:
                pass

    def fit(self, train_x, train_y):
        # train_x is a list of lists
        # train_y is a panda Series
        train_x = train_x.tolist()
        train_y = train_y.tolist()

        # Initialize the weights to be len(train_x[0]) + 1
        number_of_features = len(train_x[0])
        number_of_weights = number_of_features + 1
        weights = []
        a = 0.1                             # learning rate

        # print("number of weights are: {0}".format(number_of_weights))
        for i in range(number_of_weights):
            weights.append(0.1)
        print("weights are: {0}".format(weights))

        for number, instance in enumerate(train_x):
            # looping though each example of the training data
            instance.insert(0, 1)           # this is x0 equivalent to 1

            # use the formula: y = b0x0 + b1x1 ... bnxn
            predicted = 0                   # this is also the predicted

            for index in range(number_of_features):
                value = weights[index] * instance[index]
                predicted = predicted + value

            # Have y at this point, therefore get error (y-f(x))
            actual = train_y[number]        # this is the actual value for that instance obtained from the train_y

            error = actual - predicted
            try:
                print("Min weights before check {0}".format(self.min['weights']))
            except Exception as e:
                pass
            self.check_lowest_error(error, weights)
            print("Min weights after check {0}".format(self.min['weights']))

            # Use Widrow Hoff rule to update weight
            # new_weight = current_weight + learning_rate(actual - predicted) * training_example x
            for i in range(len(weights)):
                weights[i] = weights[i] + (a * error * instance[i])

            print("Min weights are: {0}".format(self.min['weights']))
            print("new weights are: {0}".format(weights))

    def predict(self, test_x):
        # test_x is a list of lists
        # returns y_pred which is a list
        test_x = test_x.tolist()
        print("Using weights: {0} which had an error: {1}".format(self.min['weights'], self.min['error']))
        number_of_features = len(test_x[0])

        y_pred = []                         # the list of predictions that we will return

        for number, instance in enumerate(test_x):
            instance.insert(0, 1)           # this is x0 equivalent to 1
            predicted = 0

            for index in range(number_of_features):
                value = self.min['weights'][index] * instance[index]
                predicted = + value
            y_pred.append(predicted)

        print("Returning y_pred as: {0}".format(y_pred))
        return y_pred
