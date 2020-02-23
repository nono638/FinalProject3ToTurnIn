from flask import Flask, render_template
import pandas as pd
import json
import sqlalchemy
from sqlalchemy import create_engine

#enter password for postgreSQL DB
password="smeg1205"
rds_connection_string = f"postgres:{password}@localhost:5432/SneakerData"
#MAKES ENGINE/DATABSE CONNECTION:
engine = create_engine(f'postgresql://{rds_connection_string}')
conn = engine.connect()

sneakers_query = """
    select * from public."Sneakers"
"""
sneakers_query_df = pd.read_sql(sneakers_query,conn)
sneakers_query_df = sneakers_query_df.set_index('State')
sneakers_data = sneakers_query_df.to_dict('index')

income_query = """
    select * from public."Income"
"""
income_query_df = pd.read_sql(income_query,conn)
income_query_df = income_query_df.set_index('State')
income_data = income_query_df.to_dict('index')

entireDataset = {}
entireDataset['sneakerData'] = sneakers_data
entireDataset['incomeData'] = income_data
entireDataset['statePopulations'] = {'California': 39937489, 'Texas': 29472295, 'Florida': 21992985, 'New York': 19440469, 'Pennsylvania': 12820878, 'Illinois': 12659682, 'Ohio': 11747694, 'Georgia': 10736059, 'North Carolina': 10611862, 'Michigan': 10045029, 'New Jersey': 8936574, 'Virginia': 8626207, 'Washington': 7797095, 'Arizona': 7378494, 'Massachusetts': 6976597, 'Tennessee': 6897576, 'Indiana': 6745354, 'Missouri': 6169270, 'Maryland': 6083116, 'Wisconsin': 5851754, 'Colorado': 5845526, 'Minnesota': 5700671, 'South Carolina': 5210095, 'Alabama': 4908621, 'Louisiana': 4645184, 'Kentucky': 4499692, 'Oregon': 4301089, 'Oklahoma': 3954821, 'Connecticut': 3563077, 'Utah': 3282115, 'Iowa': 3179849, 'Nevada': 3139658, 'Arkansas': 3038999, 'Puerto Rico': 3032165, 'Mississippi': 2989260, 'Kansas': 2910357, 'New Mexico': 2096640, 'Nebraska': 1952570, 'Idaho': 1826156, 'West Virginia': 1778070, 'Hawaii': 1412687, 'New Hampshire': 1371246, 'Maine': 1345790, 'Montana': 1086759, 'Rhode Island': 1056161, 'Delaware': 982895, 'South Dakota': 903027, 'North Dakota': 761723, 'Alaska': 734002, 'District of Columbia': 720687, 'Vermont': 628061, 'Wyoming': 567025}



app = Flask(__name__)

@app.route('/placeholder')
def project():
   return render_template("index.html",
   data = entireDataset)

@app.route('/map')
def map():
    return render_template("Project3.html",
    data = entireDataset)

if __name__ == "__main__": 
    app.run(debug = True)


app = Flask(__name__)