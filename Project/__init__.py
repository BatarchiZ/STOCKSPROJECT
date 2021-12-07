from flask import Flask
import pandas as pd

data = pd.read_csv(r'/Users/iskandersergazin/Desktop/financials.csv')



app = Flask(__name__)
from Project import routes



