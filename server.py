import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


regions = {'barrie': 0,
 'belleville': 1,
 'brantford': 2,
 'brockville': 3,
 'cambridge': 4,
 'chatham kent': 5,
 'city of toronto': 6,
 'cornwall on': 7,
 'gatineau': 8,
 'guelph': 9,
 'hamilton': 10,
 'kapuskasing': 11,
 'kawartha lakes': 12,
 'kingston on': 13,
 'kitchener waterloo': 14,
 'leamington': 15,
 'london': 16,
 'markham york': 17,
 'mississauga peel': 18,
 'muskoka': 19,
 'napanee': 20,
 'norfolk county': 21,
 'north bay': 22,
 'oakville halton': 23,
 'oshawa durham': 24,
 'ottawa': 25,
 'owen sound': 26,
 'peterborough': 27,
 'sarnia': 28,
 'sault ste marie': 29,
 'st catharines': 30,
 'stratford on': 31,
 'sudbury': 32,
 'thunder bay': 33,
 'timmins': 34,
 'trenton on': 35,
 'windsor area on': 36,
 'woodstock on': 37}

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


    cities, rents = getRentForEachCities(data)
    print(cities)
    print(rents)
    return render_template('rent.html',rent=rent,cities=cities,rents=rents,predicted=output)


def getRentForEachCities(data):

    features = data[:-1]
    finalInput = []
    for i in range(38):
        tempFt = features.copy()
        tempFt.append(i) # add each city names - 0 - 37
        finalInput.append(tempFt)
        tempFt=[]    

    # lets predict rent in each cities
    rent = []
    for i in range(len(finalInput)):
        #print(model.predict([y[i]]))
        rent.append(round(np.expm1(model.predict([finalInput[i]]))[0],2))

    cities = []
    for key in regions.keys():
        cities.append(key)


    return cities, rent

if __name__ == '__main__':
    app.run(port=5004, debug=True)