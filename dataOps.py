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

    def get_model(self, model_location=r'./models/model_2018_08_18_19'):
        file = open(model_location, 'rb')
        data_df = pickle.load(file)
        return data_df

    def get_prediction(self, procedure='sample', state='NY'):
        """
        Function to get the predicted values for the given procedure and state from the DB

        :param procedure: the name of the procedure (eg: 'brain surgery')
        :param state: the state (eg: NY, NJ, AZ, etc)
        :return: json object of the structure {'predicted_cost': 5000}
            the predicted_cost is always in USD for now
        """
        # get the pickled model file
        pred_model = self.get_model()
        # use the model file to make prediction
        predicted_cost = pred_model[procedure][state]
        # return prediction
        if predicted_cost:
            return json.dumps({'predicted_cost': predicted_cost, 'message': 'success'})
        else:
            fail_msg = 'No data in the predictions table for {procedure} and {state}'.format(procedure=procedure,
                                                                                             state=state)
            return json.dumps({'message': fail_msg})

    def get_all_predictions(self, procedure='sample', model_file=r'./models/model_2018_08_18_05'):
        # get the pickled model file
        pred_model = self.get_model()
        # use the model file to make prediction
        predicted_cost = pred_model[procedure]
        # return prediction
        if predicted_cost:
            return json.dumps(predicted_cost)
        else:
            fail_msg = 'No data in the predictions table for {procedure} and {state}'.format(procedure=procedure,
                                                                                             state=state)
            return json.dumps({'message': fail_msg})

        pass


