import flask
import joblib
import flask_bootstrap
from flask import request, render_template
from flask import app
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS

@app.route('/')
def home():
    return render_template('/HomePageDesign/homeIndex.html')

@app.route('/predict')
def predictPrice():

    model = joblib.load('ResaleValueModel.ml')

    carPrice = model.predict([[
    request.args['brand'],
    request.args['body'],
    request.args['mileage'],
    request.args['engineV'],
    request.args['engineType'],
    request.args['registration'],
    request.args['year'],
    request.args['model']]])

    return str(carPrice)

app.run()
