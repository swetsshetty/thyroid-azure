
# importing the necessary dependencies

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from application_logging import logger

class cassandainsert_class:
    """
      This class shall be used for handling  cassandra cloud insert data operations.

      Written By: shwetha shetty
      Version: 1.0
      Revisions: None

      """
    def __init__(self, param):
        self.param = param
        self.file_object = open("cassandra_insert_log.txt", 'a+')
        self.log_writer = logger.App_Logger()

    def cassandainsert_fnc(self):
        try:
            self.log_writer.log(self.file_object, 'cassandra cloud connection is started')
            cloud_config = {'secure_connect_bundle': 'C:\\Users\\SWETA\\secure-connect-thyroiddata.zip'}
            auth_provider = PlainTextAuthProvider('AfrUojylEzrfnACNxTkerjZC','bzQJN8CbEzc-23jQh76s67jB0CrR-bEKleGHNdtssPSSvhzCp5OIPYfS1dZ58CWe.hlA-ZPI6lkIKSLYdGSPIfWf,ICTlp_-1X9mzvmZLWE+8o7w8OjqQJ5M6P,8xfmM')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.log_writer.log(self.file_object, 'cassandra connection to keyspace is started')
            session = cluster.connect('thyroiduserdata')
            self.log_writer.log(self.file_object, 'connected  to keyspace  : thyroiduserdata')
            session.execute("insert into userinput (age,sex,TSH,TT4,T3,T4U,FTI,diagnosis) values(%s,%s,%s,%s,%s,%s,%s,%s);",self.param)
            self.log_writer.log(self.file_object, 'user input and result is inserted into  cassandra database ')
        except Exception as e:
            raise e



