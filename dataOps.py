
class dataOps(object):
    def __init__(self):
        """
        Constructor for now it doesnt have any input parameters
        """
        # ToDo: get credentials from a config file
        self.credentials = {'host': '', 'username': '', 'password': '', 'port': ''}
        pass

    def get_prediction(self, procedure, state):
        """
        Function to get the predicted values for the given procedure and state from the DB

        :param procedure: the name of the procedure (eg: 'brain surgery')
        :param state: the state (eg: NY, NJ, AZ, etc)
        :return: json object of the structure {'predicted_cost': 5000}
            the predicted_cost is always in USD for now
        """