'''
This script has a class which creates an object to store the yacht data into a database in the cloud.
The class depends on AWS RDS as the service with POSTGRESQL database
'''
from sqlalchemy import create_engine
import psycopg2


class RdsDataStorage:
    '''
    This class creates the engine for the AWS RDS
       
    '''
    def __init__(self):
        self.DATABASE_TYPE = 'postgresql'
        self.DBAPI = 'psycopg2'
        self.DATABASE = 'postgres'
        self.PORT = 5432
        
    def get_endpoint(self): 
        '''
        This function asks the user and returns their endpoint of the databas
            
            Returns:
                ENDPOINT (str): The endpoint of the users database
        '''
        print('Select postgres RDS endpoint for data storage')
        ENDPOINT = str(input('Endpoint: '))
        return ENDPOINT
    
    def get_username(self):     
        '''
        This function asks the user for the username of the database
            
            Returns:
                USER (str): The username of the users database
        '''
        print('Type username?')
        USER = str(input('Enter your username: '))
        return USER

    def get_password(self):     
        '''
        This function asks the user for password of the database
            
            Returns:
                PASSWORD (str): The password of the users database
        '''
        print('Whats your password?')
        PASSWORD = str(input('Enter your password: '))
        return PASSWORD

    def create_engine(self, ENDPOINT, USER, PASSWORD):
        '''
        This function creates the engine for the AWS RDS
        
            Attributes:
                ENDPOINT (str): The endpoint of the users database
                USER (str): The username of the users database
                PASSWORD (str): The password of the users database
         '''           
        engine = create_engine(f"{self.DATABASE_TYPE}+{self.DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{self.PORT}/{self.DATABASE}")
        return engine