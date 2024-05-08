import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn import metrics
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")

q = ""

@app.route("/")
def loadPage():
    return render_template('home.html',query="")

@app.route("/",methods=['POST'])
def predict():

    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']

    model = pickle.load(open("best_model.sav",'rb'))

    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9, inputQuery10]]
    
    new_df = pd.DataFrame(data, columns = ['Hour','temp_teenage','temp_living','humidity_out','humidity_teenage',
                            'temp_kitchen','humidity_parent','humidity_station','humidity_bath','temp_office'])
    
    scaler = MinMaxScaler()
    scaled_df = scaler.fit_transform(new_df)

    energy_predicted = model.predict(scaled_df)
    predict_energy = energy_predicted[0]
    o1 = "Energy predicted is {}".format(energy_predicted)

    return render_template('home.html', output1 = o1,
                           query1 = request.form['query1'], 
                           query2 = request.form['query2'],
                           query3 = request.form['query3'],
                           query4 = request.form['query4'],
                           query5 = request.form['query5'], 
                           query6 = request.form['query6'], 
                           query7 = request.form['query7'], 
                           query8 = request.form['query8'], 
                           query9 = request.form['query9'], 
                           query10 = request.form['query10'] )

app.run()