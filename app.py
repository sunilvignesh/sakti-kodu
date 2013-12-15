from flask import Flask
from flask import render_template
from flask.ext.pymongo import PyMongo

import utils


app = Flask("sakti_kodu")
mongo = PyMongo(app)

def mapper(entry):
	return entry["energy"]

def reducer(accumulator, data):
	result = []
	for x, y in zip(accumulator, data):
		result.append(x + y)
	return result	

@app.route("/street/<street_name>")
def street(street_name):
	
	headers = mongo.db.streetlights.aggregate(utils.street_pipeline(street_name))
	streetlights = mongo.db.streetlights.aggregate(utils.street_light_aggregator(street_name))["result"]
	
	results = map(mapper, mongo.db.streetlights.aggregate(utils.timeseries_pipeline(street_name))["result"])
	timeseries =  reduce(reducer, results)
	
	return render_template('index.html', title = "Street" , headers = headers["result"][0], streetlights = streetlights, timeseries = timeseries)
	
@app.route("/ward/<ward_number>")
def ward(ward_number):
	headers = mongo.db.streetlights.aggregate(utils.ward_pipeline(ward_number))
	streetlights = mongo.db.streetlights.find({"ward": ward_number})

	return render_template('index.html', tittle = "Ward", headers = headers["result"][0], streetlights = utils.to_list(streetlights))

@app.route("/district/<district_name>")
def district(district_name):
	headers = mongo.db.streetlights.aggregate(utils.district_pipeline(district_name))
	streetlights = mongo.db.streetlights.find({"district": district_name})

	print headers
	return render_template('index.html', title = "District" , headers = headers["result"][0], streetlights = utils.to_list(streetlights))
        
if __name__ == "__main__":
    app.run(debug = True)