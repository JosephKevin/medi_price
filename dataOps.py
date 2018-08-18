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
        # get the pickled model file
        pred_model = pickle.load(model_file)
        # use the model file to make prediction
        predicted_cost = pred_model.predict([procedure, state])
        # return prediction
        if predicted_cost:
            return json.dumps({'predicted_cost': predicted_cost, 'message': 'success'})
        else:
            fail_msg = 'No data in the predictions table for {procedure} and {state}'.format(procedure=procedure,
                                                                                             state=state)
            return json.dumps({'message': fail_msg})

    def get_predictions_all(self, procedure='sample', model_file=r'./models/model_2018_08_18_05'):

        pass


