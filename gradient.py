import numpy as np
import logging
from cloghandler import ConcurrentRotatingFileHandler

logger = logging.getLogger(__name__)

handler = ConcurrentRotatingFileHandler('gradient.log', "a", 1024*1024*1024*3, 1000)
formatter = logging.Formatter(
    '%(asctime)s] - %(name)s - %(levelname)s in %(module)s:%(lineno)d:%(funcName)-10s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


class GradientDescent:
    def __init__(self):
        self.weights = []
        self.lowest_weights = []
        self.min_error = None

    def __del__(self):
        self.weights = []
        self.lowest_weights = []
        self.min_error = None

    def check_lowest_error(self, error, weights):
        if not self.min_error:
            self.min_error = error
            self.lowest_weights = weights
            print("Minimum error is now: {0} and using weights: {1}".format(self.min_error, self.lowest_weights))
        else:
            if self.min_error > error:
                self.min_error = error
                self.lowest_weights = weights
                print("Minimum error is now: {0} and using weights: {1}".format(self.min_error, self.lowest_weights))

    def fit(self, train_x, train_y):
        # train_x is a list of lists
        # train_y is a panda Series
        train_x = train_x.tolist()
        train_y = train_y.tolist()

        # Initialize the weights to be len(train_x[0]) + 1
        number_of_features = len(train_x[0])
        number_of_weights = number_of_features + 1
        a = 0.1                             # learning rate

        # print("number of weights are: {0}".format(number_of_weights))
        for i in range(number_of_weights):
            self.weights.append(0.1)
        print("weights are: {0}".format(self.weights))

        for number, instance in enumerate(train_x):
            # looping though each example of the training data
            instance.insert(0, 1)           # this is x0 equivalent to 1

            # use the formula: y = b0x0 + b1x1 ... bnxn
            predicted = 0                   # this is also the predicted

            for index in range(number_of_features):
                value = self.weights[index] * instance[index]
                predicted =+ value

            # Have y at this point, therefore get error (y-f(x))
            actual = train_y[number]        # this is the actual value for that instance obtained from the tain_y

            error = actual - predicted
            print("Error for this instance was: {0}".format(error))
            self.check_lowest_error(error, self.weights)
            # print("Error for this example is: {0}".format(error))

            # Use Widrow Hoff rule to update weight
            # new_weight = current_weight + leaning_rate(actual - predicted) * training_example x
            for i in range(len(self.weights)):
                new_weight = self.weights[i] + (a * error * instance[i])
                self.weights[i] = new_weight
            print("new weights are: {0}".format(self.weights))

    def predict(self, test_x):
        # test_x is a list of lists
        # returns y_pred which is a list
        test_x = test_x.tolist()
        print("Using weights: {0} which had an error: {1}".format(self.lowest_weights, self.min_error))
        number_of_features = len(test_x[0])

        y_pred = []                         # the list of predictions that we will return

        for number, instance in enumerate(test_x):
            instance.insert(0, 1)           # this is x0 equivalent to 1
            predicted = 0

            for index in range(number_of_features):
                value = self.lowest_weights[index] * instance[index]
                predicted = + value
            y_pred.append(predicted)

        print("Returning y_pred as: {0}".format(y_pred))
        return y_pred
