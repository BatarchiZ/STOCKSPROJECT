from flask import Flask
import pandas as pd

url = 'https://github.com/BatarchiZ/STOCKSPROJECT/blob/master/Project/financials.csv'
data = pd.read_csv('financials.csv')



app = Flask(__name__)
from Project import routes



