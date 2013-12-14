from flask import Flask
from flask import render_template
from flask.ext.pymongo import PyMongo

import utils


app = Flask("sakti_kodu")
mongo = PyMongo(app)

@app.route("/street/<street_name>")
def street(street_name):
	headers = mongo.db.streetlights.aggregate(utils.streets_pipeline(street_name))
	streetlights = mongo.db.streetlights.find({"street": street_name})
	
	return render_template('index.html', headers = headers, streetlights = to_list(streetlights))

@app.route("/ward/<ward_number>")
def ward(ward_number):
	pass

@app.route('/')
def all():
	return str(to_list(mongo.db.streetlights.find()))

def to_list(cursor):
       records = []
       for record in cursor:
               records.append(record)
       return records        

if __name__ == "__main__":
    app.run(debug = True)