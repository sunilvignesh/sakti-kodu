from flask import Flask
from flask import render_template
from flask.ext.pymongo import PyMongo


app = Flask("sakti_kodu")
mongo = PyMongo(app)

@app.route("/street/<street_name>")
def street(street_name):
	pipeline = [{"$match":{"street":street_name}},{"$group":{"_id":"street","total":{"$sum":1},"energy_dist":{"$addToSet": "$energy"}}}, { "$project" : {
        "streetlights" : "$total" ,
        "total_energry" : "$energy" ,
        "total_power" : "$power",
        "energy_dist" : "$energy_dist"
    }}]
	
	data_agg = mongo.db.streetlights.aggregate(pipeline)
	print str(data_agg["result"])
	return render_template('index.html', aggregate = data_agg["result"])

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