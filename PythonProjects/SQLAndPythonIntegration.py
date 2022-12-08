#pip install pyodbc
#pip install pandas

import pyodbc
import pandas as pd

query1 = "SELECT TOP 1 * FROM dbo.[TABELA DE CLIENTES]"
query2 = "SELECT * FROM dbo.[TABELA DE PRODUTOS];"

def create_connection():
    abountConnection = (
        "Driver={SQL Server};"
        "Server=PRONBK-23\SERVIDOR_TESTE;"
        "Database=SUCOS_VENDAS_V3;"
        "Trusted_Connection=yes;" #Access the database with windows authentication
    )

    connection = pyodbc.connect(abountConnection)
    return connection


def quering_database(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)

    print('\n')
    print('Select into python')

    for i in cursor:
        print(i)
    print('\n')


def inserting_into_dataframe(query):
    connection = create_connection()
    query = query2
    dataset = pd.read_sql(query, connection)

    print('\n')
    print('Dataframe Pandas')
    print(dataset.head())


quering_database(query1)
inserting_into_dataframe(query2)