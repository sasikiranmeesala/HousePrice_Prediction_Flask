from flask import Flask,render_template,request
import pickle
import numpy as np
# create an object
application = Flask(__name__)
'''
@application.route('/')
def hello():
    """test funtion"""
    return "welcome to the Flask"


@application.route('/sasi',methods=['GET'])
def check():
    """new function"""
    return "Hello, There"
'''
#first lets read the pickle file
with open('House_price.pkl','rb') as f:
    model = pickle.load(f)

@application.route('/',methods=['GET'])
def home():
    return render_template('index.html') # it is available from jinga template

@application.route('/predict',methods=['POST'])
def predict():
    Rooms = int(request.form['bedrooms'])
    Bathrooms  = int(request.form['bathrooms'])
    Place = int(request.form['location'])
    Area  = int(request.form['area'])
    Status = int(request.form['status'])
    Facing = int(request.form['facing'])
    p_Type = int(request.form['type'])
    # now take the above form of data an d convert to array
    input_data = np.array([[Place, Area, Status, Rooms, Bathrooms, Facing, p_Type]])
    # by taking above data we will predict the House_price
    prediction = model.predict(input_data)[0]
    #now we will pass the above predicted to template
    return render_template('index.html',prediction = prediction)
            
application.run()
