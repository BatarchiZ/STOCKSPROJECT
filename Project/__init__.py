from flask import Flask
import pandas as pd

data = pd.read_csv('financials.csv')



app = Flask(__name__)
from Project import routes



