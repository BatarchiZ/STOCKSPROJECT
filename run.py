from flask import Flask
import pandas as pd

data = pd.read_csv('/Users/iskandersergazin/Desktop/HSE Python/STOCKSPROJECT/Project/data/financials.csv')



app = Flask(__name__)

if __name__== '__main__':
    app.run()