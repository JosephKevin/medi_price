import pickle
import datetime
import pymysql
import json
import os


class build_model(object):
    def __init__(self):
        pass

    def build_dt_regressor(self, db_schema, raw_data, input_features, creds_file=r'../creds.json',
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
        :param creds_file: the file with the DB credentials
        :return: No return
        """
        with open(creds_file) as f:
            credentials = json.load(f)
        # 1. make DB connection
        connection = pymysql.connect(host=credentials['host'],
                                     user=credentials['username'],
                                     password=credentials['password'],
                                     db='medical_data',
                                     cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # 2. get raw_data from the DB
                sql = "SELECT * from `raw_data`"
                cursor.execute(sql)
                result = cursor.fetchone()
        finally:
            # 3. close connection
            connection.close()
        # 4. build model
        # ToDo build model
        # 5. pickle model
        model_file_name = 'model' + datetime.datetime.today().strftime('%Y_%m_%d_%H')
        model_file = os.path.store(model_store, model_file_name)
        pred_model = ''
        filehandler = open(model_file, "wb")
        pred_model_pickle = pickle.dump(obj=pred_model, file=filehandler)

if __name__ == '__main__':
    bm = build_model()
    bm.build_dt_regressor()
