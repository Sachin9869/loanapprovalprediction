# -*- coding: utf-8 -*-

from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.embed import components

app=Flask(__name__)

@app.route('/')

def home():
  return render_template('index.html')

@app.route('/Main')
def Main():
  return (render_template('index.html'))

@app.route('/result',methods=['POST'])

@app.route("/Individual", methods=['GET', 'POST'])

def Individual():
  if request.method == 'GET':
    return (render_template('Individual.html'))

  loan_id=request.form['LoanId']
  gender=request.form['Gender']
  married = request.form['Married']
  dependents=request.form['Dependents']
  education=request.form['Education']
  self_employed=request.form['SelfEmployed']
  app_income=request.form['AppIncome']
  coapp_income=request.form['CoAppIncome']
  loan_amt=request.form['LoanAmount']
  loan_amount_term=request.form['LoanId']
  credit_hist=request.form['CreditHistory']
  prop_area=request.form['PropertyArea'] 
  
  
  #  creating a json object to hold the data from the form
  input_data=[{
  'loan_id':loan_id,
  'gender':gender,
  'married':married,
  'dependents':dependents,
  'education':education,
  'self_employed':self_employed,
  'app_income':app_income,
  'coapp_income':coapp_income,
  'loan_amt':loan_amt,
  'loan_amount_term':loan_amount_term,
  'credit_hist':credit_hist,
  'prop_area':prop_area}]

  dataset=pd.DataFrame(input_data)

  dataset=dataset.rename(columns={
      'loan_id':'Loan_ID',
      'gender': 'Gender',
      'married':'Married',
      'dependents':'Dependents',
      'education':'Education',
      'self_employed':'Self_Employed',
      'app_income':'ApplicantIncome',
      'coapp_income':'CoapplicantIncome',
      'loan_amt':'LoanAmount',
      'loan_amount_term':'Loan_Amount_Term',
      'credit_hist':'Credit_History',
      'prop_area':'Property_Area'})
  
  dataset[['CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']] = dataset[['CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']].astype(float)

  dataset[['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']] = dataset[['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']].astype(object)

  dataset[['ApplicantIncome']] = dataset[['ApplicantIncome']].astype(int)

  dataset = dataset[['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']]
  
  model = pickle.load(open('loan_predict.pkl', 'rb'))

  classifier=model.predict(dataset)

  if classifier == 'Y':
    res = 'Congratulations! Your loan is approved. Kindly connect with support team for paper work'
  else:
    res = 'Loan Denied'  

  return render_template('Individual.html',
                               result=res)    
