from flask import Flask, request, jsonify, render_template
import json
import pickle


class dataOps(object):
    def __init__(self):
        """
        Constructor for now it doesnt have any input parameters
        """
        with open(r'./creds.json') as f:
            self.credentials = json.load(f)

    def get_prediction(self, procedure='sample', state='NY', model_file=r'./models/model_2018_08_18_05'):
        """
        Function to get the predicted values for the given procedure and state from the DB

        :param procedure: the name of the procedure (eg: 'brain surgery')
        :param state: the state (eg: NY, NJ, AZ, etc)
        :param model_file: the pickled model file location
        :return: json object of the structure {'predicted_cost': 5000}
            the predicted_cost is always in USD for now
        """
<<<<<<< Updated upstream
        # get the pickled model file
        pred_model = pickle.load(model_file)
        # use the model file to make prediction
        predicted_cost = pred_model.predict([procedure, state])
        # return prediction
        if predicted_cost:
            return json.dumps({'predicted_cost': predicted_cost, 'message': 'success'})
=======
        # 1. connect to the DB
        connection = pymysql.connect(host=self.credentials['host'],
                                     user=self.credentials['username'],
                                     password=self.credentials['password'],
                                     db='medical_data',
                                     cursorclass=pymysql.cursors.DictCursor)
        # 2. get the prediction for given procedure and state
        get_pred_cost_sql = "select `Average Total Payments` from price_prediction where `DRG Definition` = \'{procedure}\' and `Provider State` = \'{provider_state}\' ".format(procedure=procedure, provider_state=state)
        try:
            with connection.cursor() as cursor:
                cursor.execute(get_pred_cost_sql)
                result = cursor.fetchone()
        finally:
            connection.close()
        # 3. return the predicted_cost
        if result:
            return json.dumps({'predicted_cost': result['Average Total Payments'], 'message': 'success'})
>>>>>>> Stashed changes
        else:
            fail_msg = 'No data in the predictions table for {procedure} and {state}'.format(procedure=procedure,
                                                                                             state=state)
            return json.dumps({'message': fail_msg})
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes


""" Flask code for the API """
app = Flask(__name__)


@app.route('/predict_price', methods=['POST'])
def predict_price():
    prediction_request = request.get_json(force=True)
    predictor = dataOps()
    predicted_price = predictor.get_prediction(prediction_request['procedure'], prediction_request['state'])
    return jsonify(predicted_price)


@app.route('/', methods=['POST', 'GET'])
def run_app():
    return render_template('testxhr.html')


if __name__ == '__main__':
    app.run()
