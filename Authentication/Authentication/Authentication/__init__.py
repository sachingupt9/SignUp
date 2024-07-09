from flask import Flask
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Define the connection string
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-81C58CO\\SQLEXPRESS;"  
    "DATABASE=MyDatabase;"  
    "UID=SPIDER;" 
    "PWD=123"  
)

def get_db_connection():
    conn = pyodbc.connect(connection_string)
    return conn

import Authentication.views

if __name__ == '__main__':
    app.run(debug=True)
