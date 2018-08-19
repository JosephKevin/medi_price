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

    def get_latest_model(self):
        #ToDo: get the lates model name
        pass

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
        # check if the dataframe has that procedure and state
        try:
            predicted_cost = pred_model[procedure][state]
        except:
            return json.dumps({'message': 'failed'})
        # return prediction
        if predicted_cost:
            return json.dumps({'predicted_cost': predicted_cost, 'message': 'success'})
        else:
            fail_msg = 'No data in the predictions table for {procedure} and {state}'.format(procedure=procedure,
                                                                                             state=state)
            return json.dumps({'message': fail_msg})

    def get_all_predictions(self, procedure='sample'):
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
        predicted_cost = pred_model[procedure].to_json()
        # return prediction
        if predicted_cost:
            return predicted_cost
        else:
            fail_msg = 'No data in the predictions table for {procedure}'.format(procedure=procedure)

            return json.dumps({'message': fail_msg})


