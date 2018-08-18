import pickle
import datetime
import pymysql
import json
import os
import pandas as pd


class build_model(object):
    def __init__(self):
        pass

    def build_dt_regressor(self, db_schema, raw_data, input_features, target, creds_file=r'../creds.json',
                           model_store=r'./models/'):
        """
        Function to
            1. make DB connection
            2. get raw_data from the DB
            3. close connection
            4. build model
            5. pickle model
            6. save model to model_store

        :param db_schema: the db schema where the raw_data table is present
        :param raw_data: the raw_data table
        :param input_features: the features to be used for the prediction
        :param target: the target to be predicted
        :param creds_file: the file with the DB credentials
        :return: No return
        """

        # 4. build model
        # ToDo build model
        self.build_model(db_schema=db_schema, raw_data=raw_data, input_features=input_features, creds_file=creds_file,
                         model_type='segmentation')
        # 5. pickle model
        model_file_name = 'model' + datetime.datetime.today().strftime('%Y_%m_%d_%H')
        model_file = os.path.store(model_store, model_file_name)
        pred_model = ''
        filehandler = open(model_file, "wb")
        pickle.dump(obj=pred_model, file=filehandler)


    def build_model(self, db_schema, raw_data, input_features, creds_file, model_type='segmentation'):
        """
        Function to handle model building

        :param db_schema: the db schema where the raw_data table is present
        :param raw_data: the raw_data table
        :param input_features: the features to be used for the prediction
        :param creds_file: the file with the DB credentials
        :param model_type: the type of model to be built
        :return: {model: model_object, message: 'success' or 'failure'}
        """
        if model_type == 'segmentation':
            return self.build_segmentation_model(db_schema, raw_data, input_features, creds_file)
        else:
            return json.dumps({'message': 'please provide a valid model type'})

    def build_segmentation_model(self, db_schema, raw_data, input_features, creds_file):
        """
        Function to build a segment model

        :param db_schema: the db schema where the raw_data table is present
        :param raw_data: the raw data table
        :param input_features: the features to be used for the prediction
        :param creds_file: the file with the DB credentials
        :return: a pandas dataframe with segment level data
        """
        with open(creds_file) as f:
            credentials = json.load(f)
        # 1. make DB connection
        connection = pymysql.connect(host=credentials['host'],
                                     user=credentials['username'],
                                     password=credentials['password'],
                                     db=db_schema,
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            sql = "SELECT * from `{raw_data}`".format(raw_data=raw_data)
            raw_data_df = pd.read_sql(sql, connection)
        finally:
            # 3. close connection
            connection.close()
        # 4. do segmentation


if __name__ == '__main__':
    bm = build_model()
    bm.build_dt_regressor()
