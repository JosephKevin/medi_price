from flask import Flask, request, jsonify, render_template
from dataOps import dataOps
""" Flask code for the API """
app = Flask(__name__)


@app.route('/predict_price', methods=['POST'])
def predict_price():
    """
    This function returns the predicted price from the ML model to the frontend.
    It takes a json object as a request body and this JSON object contains the following parameters:
        1. Procedure: The medical procedure the patient wants to know the cost of.
        2. State: The US state that the patient wants to do this procedure in.

    :return: the predicted price from the ML model
    """
    prediction_request = request.get_json(force=True)
    predictor = dataOps()
    predicted_price = predictor.get_prediction(prediction_request['procedure'], prediction_request['state'])

    return jsonify(predicted_price)

@app.route('/predict_price_all', methods=['POST'])
def predict_price_all_states():
    """
    This function returns the predicted price for all States from the ML model to the frontend.
    It takes a json object as a request body and this JSON object contains the following parameters:
        1. Procedure: The medical procedure the patient wants to know the cost of.

    :return: the predicted price from the ML model
    """
    prediction_request = request.get_json(force=True)
    predictor = dataOps()
    predicted_all_price = predictor.get_all_predictions(prediction_request['procedure'])
    return jsonify(predicted_all_price)

@app.route('/', methods=['POST', 'GET'])
def run_app():
    """
    This is the method that runs whenever someone opens the webpage.
    It renders the frontend content.
    :return: HTML page
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
