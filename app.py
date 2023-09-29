import numpy as np
import scipy as sp
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, static_folder='static')
model = pickle.load(open('model.pkl', 'rb'))

# Route for the home page
@app.route('/')
def home():
    return render_template('hey0.html')

# Route for the main page
@app.route('/index')
def index():
    return render_template('index.html')

# Route for making predictions
@app.route('/predict', methods=['POST', 'GET'])
def predict():
   
    a = request.form.get("A")
    bt = request.form['B']
    dr = request.form.get('D')
    dp = request.form['De']
    dfh = request.form.get("DFH")
    e = request.form.get("E")
    ef = request.form['EF']
    es = request.form.get("ES")
    g = request.form['G']
    hr = request.form.get("HR")
    ji = request.form.get("JI")
    jl = request.form.get("JL")
    jr = request.form['JR']
    js = request.form.get("JS")
    ms = request.form['M']
    mi = request.form.get("MI")
    ncw = request.form.get("NCW")
    ot = request.form['OT']
    pr = request.form.get("PR")
    rs = request.form.get("RS")
    sol = request.form.get("SOL")
    twy = request.form.get("TWY")
    ttl = request.form.get("TTL")
    ttlr = request.form.get("TTLR")
    wl = request.form.get("WL")
    yac = request.form.get("YAC")
    yicr = request.form.get("YICR")
    yslp = request.form.get("YSLP")
    ywcm = request.form.get("YWCM")

    
    input_dict = {
        'A': int(a),
        'B': str(bt),
        'D': int(dr),
        'De': dp,
        'DFH': int(dfh),
        'E': int(e),
        'EF': str(ef),
        'ES': int(es),
        'G': str(g),
        'HR': int(hr),
        'JI': int(ji),
        'JL': int(jl),
        'JR': jr,
        'JS': int(js),
        'M': str(ms),
        'MI': int(mi),
        'NCW': int(ncw),
        'OT': str(ot),
        'PR': int(pr),
        'RS': int(rs),
        'SOL': sol,
        'TWY': int(twy),
        'TTL': ttl,
        'TTLR': ttlr,
        'WL': int(wl),
        'YAC': int(yac),
        'YICR': int(yicr),
        'YSLP': int(yslp),
        'YWCM': int(ywcm)
    }

    # Create a DataFrame from the input dictionary
    df = pd.DataFrame([input_dict])

 

    # Make predictions
    prediction = model.predict(df)

   
    if prediction == 0:
        return render_template('index.html', prediction_text='Result A')

    else:
        return render_template('index.html', prediction_text='Result B')

if __name__ == "__main__":
    app.run()
