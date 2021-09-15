from flask import Flask, render_template, redirect, request
import joblib
import numpy as np
import logging
import sys
import os

model= joblib.load('model.pkl')

#__name__ == __main__
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def prediction():
    if request.method=="POST":
        temp=float(request.form['Temperature'])
        massloss=float(request.form['Mass Loss'])
        density=float(request.form['Density'])
        porosity=float(request.form['Porosity'])
        pwave=float(request.form['P-Wave'])
        swave=float(request.form['S-Wave'])
        ed=float(request.form['Ed'])
        
        para=np.array([temp, massloss, density, porosity, pwave, swave, ed])
        para=para.reshape(1,-1)
        thermalcoefficient= str(model.predict(para)[0])
    
    return render_template("index.html", tc= thermalcoefficient)

@app.route('/howitworks.html')
def hel():
    return render_template("howitworks.html")

@app.route('/contact.html')
def hell():
    return render_template("contact.html")

@app.route('/index.html')
def hl():
    return render_template("index.html")


if __name__=='__main__':
    #app.debug = True
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    
    print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
    print("PATH:", os.environ.get('PATH'))
    app.run(debug = False)
    
    
 