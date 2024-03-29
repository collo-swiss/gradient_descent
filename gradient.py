class GradientDescent:
    def __init__(self):
        self.min = None
        self.weights = []

    def __del__(self):
        self.min = None
        self.weights = []

    def check_lowest_error(self, error, weights, epoch):
        if not self.min:
            self.min = {
                "error": error,
                "weights": weights,
                "epoch": epoch
            }
            print("Minimum error is now: {0} and using weights: {1}".format(self.min['error'], self.min['weights']))
        else:
            if abs(self.min['error']) > abs(error):
                self.min['error'] = error
                self.min['weights'] = list(weights)
                self.min['epoch'] = epoch
                print("Minimum error is now: {0} and using weights: {1}".format(self.min['error'], self.min['weights']))
            else:
                pass

    def fit(self, train_x, train_y, epochs=1000):
        # train_x is a list of lists
        # train_y is a panda Series
        train_x = train_x.values.tolist()
        train_y = train_y.tolist()

        # Initialize the weights to be len(train_x[0]) + 1
        number_of_features = len(train_x[0])
        number_of_weights = number_of_features + 1
        a = 0.0001                             # learning rate

        # print("number of weights are: {0}".format(number_of_weights))
        for i in range(number_of_weights):
            self.weights.append(0.1)
        print("weights are: {0}".format(self.weights))

        for epoch in range(epochs):
            weights_updates = []                # Store total updates for each weight per epoch
            for i in range(number_of_weights):
                weights_updates.append(0)

            for number, instance in enumerate(train_x):
                predicted = 0                   # this is also the predicted

                # looping though each example of the training data
                instance.insert(0, 1)           # this is x0 equivalent to 1

                # use the formula: y = b0x0 + b1x1 ... bnxn
                for index in range(number_of_features):
                    value = self.weights[index] * instance[index]
                    predicted = predicted + value

                # Have y at this point, therefore get error (y-f(x))
                actual = train_y[number]        # this is the actual value for that instance obtained from the train_y

                error = actual - predicted
                self.check_lowest_error(error, self.weights, epoch)

                # Use Widrow Hoff rule to update weight
                # new_weight = current_weight + learning_rate(actual - predicted) * training_example x
                for i in range(len(self.weights)):
                    update = error * instance[i]
                    # self.weights[i] = self.weights[i] + (a * error * instance[i])
                    weights_updates[i] += update
                print("Weight updates are: {0}".format(weights_updates))
            for j in range(len(self.weights)):
                self.weights[j] = self.weights[j] + a * weights_updates[j]
            print("new weights at epoch: {0}, are: {1}".format(epoch, self.weights))

    def predict(self, test_x):
        # test_x is a list of lists
        # returns y_pred which is a list
        test_x = test_x.values.tolist()
        print("Using weights: {0}, the minimum error during training was: {1} at epoch: {2}".format(
            self.weights, self.min['error'], self.min['epoch']))
        number_of_features = len(test_x[0])

        y_pred = []                         # the list of predictions that we will return

        for number, instance in enumerate(test_x):
            instance.insert(0, 1)           # this is x0 equivalent to 1
            predicted = 0

            for index in range(number_of_features):
                value = self.weights[index] * instance[index]
                predicted = + value
            y_pred.append(predicted)

        print("Returning y_pred as: {0}".format(y_pred))
        return y_pred
