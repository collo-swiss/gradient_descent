class GradientDescent:
    def __init__(self):


    def fit(self, train_x, train_y):
        # train_x is a list of lists
        # train_y is a panda Series

        # Initialize the weights to be len(train_x[0]) + 1
        number_of_features = len(train_x[0])
        number_of_weights = number_of_features + 1
        weights = []
        for weight in range(number_of_weights):
            weights[weight] = 0.1
        print("weights are: {0}".format(weights))

        for instance in train_x:
            # looping though each example of the training data
            instance.insert(0, 1)

            # use the formula: y = b0x0 + b1x1 ... bnxn
            

        print("fit")

    def predict(self, test_x):
        # test_x is a list of lists
        # returns y_pred which is a list
        print("predict")
