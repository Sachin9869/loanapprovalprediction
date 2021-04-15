# -*- coding: utf-8 -*-

from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.embed import components

app=Flask(__name__)

if __name__ == "__main__":
 app.run()

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/Main')
def Main():
  return (render_template('index.html'))

#@app.route('/result',methods=['POST'])

@app.route("/Individual", methods=['GET', 'POST'])

def Individual():
  if request.method == 'GET':
    return (render_template('Individual.html'))


  features = [float(i) for i in request.form.values()]
  array_features = [np.array(features)]
  model = pickle.load(open('loan_predict.pkl', 'rb'))

  classifier=model.predict(dataset)

  if classifier == 1:
    res = 'Congratulations! Your loan is approved. Kindly connect with support team for paper work'
  else:
    res = 'Loan Denied'  

  return render_template('Predresult.html',
                         result = res)
 

