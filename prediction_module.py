from datetime import datetime
from application_logging import logger
import pickle

class pred_class:
    def __init__(self,value):
        self.value = value
        self.file_object = open("pred_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def pred_fnc(self):
        try:
            self.log_writer.log(self.file_object,'Start of prediction !!')
            loaded_model = pickle.load(open('decisiontree_model1.pickle', 'rb')) # loading the model file from the storage
            self.log_writer.log(self.file_object, ' pickle file for prediction  is loaded !!')
            # predictions using the loaded model file
            pred=loaded_model.predict([self.value])
            self.log_writer.log(self.file_object, '  prediction complete !!')
            print( 'predicted value from the module is  !!',pred)
        except Exception as e:
            raise e
        return pred








