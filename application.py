
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from prediction_module import pred_class


application = Flask(__name__) # initializing a flask app
app=application

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            age = int(request.form.get('age'))
            sex = float(request.form.get('sex'))
            TSH = float(request.form.get('TSH'))
            T4U = float(request.form.get('T4U'))
            T3 = float(request.form.get('T3'))
            TT4 = float(request.form.get('TT4'))
            FTI = float(request.form.get('FTI'))
            value= [age,sex,TSH,T3,TT4,T4U,FTI]
            pred=pred_class(value)
            pred_value=pred.pred_fnc()
            if pred_value == 0:
                res_val = "hyperthyroidism"
            elif pred_value == 1:
                res_val = "hypothyroidism"
            elif pred_value == 2:
                res_val = "no thyroid"
            print('The patient has ', res_val)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=res_val)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app