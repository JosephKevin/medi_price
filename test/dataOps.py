from flask import Flask, request, jsonify
import json
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
        return json.dumps({'price': 120})


""" Flask code for the API """
app = Flask(__name__)


@app.route('/predict_price', methods=['POST'])
def predict_price():
    prediction_request = request.get_json(force=True)
    predictor = dataOps()
    predicted_price = predictor.get_prediction(prediction_request['procedure'], prediction_request['state'])
    return jsonify(predicted_price)


if __name__ == '__main__':
    app.run()
