from flask import Flask, render_template , request
import numpy as np
import pandas as pd
import joblib


app=Flask(__name__)


@app.route("/")
def home():
    return render_template("sentiment.html")
    
@app.route("/prediction",methods=["get","post"])
def prediction():
    t=request.form.get("review")
    if request.method == 'POST':
        name = request.form['name']

        review = request.form['review']
    rev=pd.Series(t)
    model=joblib.load("Best_models1/logistic_regression.pkl")

    prediction=model.predict(rev)

    return render_template("output.html",prediction=prediction , name=name,review=review)

if __name__ == "__main__" :
    app.run(debug=True,host="0.0.0.0",port=5000)   

