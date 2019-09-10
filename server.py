import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__,template_folder='template')

# Load the model
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    print(data)
    #prediction = model.predict([[np.array(data['exp'])]])
    prediction = model.predict([data['exp']])

    # Take the first value of prediction
    output = prediction[0]

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5003, debug=True)