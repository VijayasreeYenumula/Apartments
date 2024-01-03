from  flask import Flask,render_template,request
from args import *
import numpy as np
import pickle
with open('Model.pkl','rb') as mod:
    model=pickle.load(mod)
with open('Scaler.pkl','rb') as mod:
    scaler=pickle.load(mod)
app=Flask(__name__)#it mainly used for default
#it uses mainly for easy debuging
@app.route('/',methods=['GET','POST'])#route --
#@--2 type centralized and
#@--with out changing the function  it extends the old version & new version
def index():
    # print(request.method)
    # print(request.form)
    #return 'i'm in first page'
    if request.method=='POST':
        bedrooms=request.form['bedrooms']
        bathrooms=request.form['bathrooms']
        location=request.form['location']
        Sqft=request.form['Sqft']
        status=request.form['status']
        direction=request.form['direction']
        property_type=request.form['property_type']
        input_array=np.array([[
            bedrooms,bathrooms,location,Sqft,status,direction,property_type
        ]])
        t_array=scaler.transform(input_array)
        prediction=model.predict(t_array)[0]
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               direction_mapping=direction_mapping
                               ,property_type_mapping=property_type_mapping,
                               prediction=prediction)
    else:
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               direction_mapping=direction_mapping
                               ,property_type_mapping=property_type_mapping)
    
@app.route('/second')
def second():
    return 'Iam in second page'
@app.route('/third')
def third():
    return 'Iam in third page'
app.run(use_reloader=True,debug=True)#debug only for testing


