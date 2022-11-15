# Import packages
import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

# Load our .env file from the path
dotenv_path=os.path.abspath('./config.env')
load_dotenv(dotenv_path)

# Define environment variables
dbname = os.getenv('DBNAME')
user = os.getenv('DBUSER')
pw = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
 
def conn():
    # Basic connector
    try:
        conn = psycopg2.connect(database=dbname,
                                user=user,
                                password=pw,
                                host=host,
                                port=port)
        connection, cursor = conn, conn.cursor()
        print("Database connection successful")
        return connection, cursor 
    except Exception as e:
        print("Database connection failed. Error: ", e)

    
def get_query(sql):
    '''
    A function that takes in an SQL string, queries from PostgreSQL and returns the result in a Pandas dataframe.
    sql: SQL Query eg. "SELECT * FROM person"
    returns: Pandas DF
    '''
    connection, cursor = conn()
    cursor.execute(sql)
    data = cursor.fetchall()

    cols = []
    for elt in cursor.description:
        cols.append(elt[0])

    df = pd.DataFrame(data=data, columns=cols)
    connection.close()
    return df


def get_person(person_list):
    '''
    A function that takes in a list of persons, queries from PostgreSQL and returns the result in a Pandas dataframe.
    person_list: List of persons eg. [1000,2000,3000]
    returns: Pandas DF
    '''
    sql_string = '''
    SELECT * FROM synthea_native.patients
    WHERE id IN (%s)
    '''

    connection, cursor = conn()
    cursor.execute(sql_string, person_list)
    data = cursor.fetchall()

    cols = []
    for elt in cursor.description:
        cols.append(elt[0])

    df = pd.DataFrame(data=data, columns=cols)
    connection.close()
    return df
