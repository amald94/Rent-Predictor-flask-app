import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__,template_folder='template')

# Load the model
model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/getrent',methods=['POST'])
def getrent():

    # Get the data from the POST request.
    unit = int(request.form['unitSelected'])
    bed = int(request.form['bedSelected'])
    bath = int(request.form['bathSelected'])
    pet = int(request.form['petSelected'])
    fur = int(request.form['furSelected'])
    park = int(request.form['parSelected'])
    air = int(request.form['airSelected'])
    smo = int(request.form['smoSelected'])
    region = int(request.form['regSelected'])

    #data = request.get_json(force=True)
    data = [unit,bed,bath,pet,fur,park,air,smo,region]
    print(data)
    # Make prediction using model loaded from disk as per the data.
    #print(data)
    #prediction = model.predict([[np.array(data['exp'])]])
    prediction = model.predict([data])

    # Take the first value of prediction
    output = prediction[0]
    output = round(np.expm1(output),2)
    rent = '$ '+str(output)
    return render_template('rent.html',rent=rent)

if __name__ == '__main__':
    app.run()
