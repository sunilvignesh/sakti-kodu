def street_pipeline(street_name):
	return [{"$match":
		{"street":street_name}},
		{"$group": {"_id":"$id", "energy" : {"$last" : "$energy"}, "power" : {"$last" : "$power"}, "luminance": {"$last": "$luminance"}}},
		{"$group":{"_id":"street","streetlights":{"$sum":1},"total_energy":{"$sum":"$energy"}, "total_power":{"$sum":"$power"}, "energy_dist":{"$addToSet": "$energy"}, "total_luminance": { "$avg": "$luminance"}}}]

def street_light_aggregator(street_name):
	return [{"$match":
		{"street":street_name}},
		{"$group": {"_id":"$id", "energy" : {"$last" : "$energy"}, "power" : {"$last" : "$power"}, "luminance": {"$last": "$luminance"},"status": {"$last": "$status"},"id": {"$last": "$id"}}}, { "$sort" : {"id": 1}}]

def timeseries_pipeline(street_name):
	  return [{"$match":
		{"street":street_name}},
		{"$group": {"_id":"$id", "energy" : {"$addToSet" : "$energy"}}}]

def flat():
	pass

def ward_pipeline(ward_number):
	return [{"$match":{"ward":ward_number}},
	{"$group":{"_id":"street","streetlights":{"$sum":1},"total_energy":{"$sum":"$energy"}, "total_power":{"$sum":"$power"}, "energy_dist":{"$addToSet": "$energy"}, "total_luminance": { "$avg": "$luminance"}}}]

def district_pipeline(district_name):
	return [{"$match":{"district":district_name}},
	{"$group":{"_id":"street","streetlights":{"$sum":1},"total_energy":{"$sum":"$energy"}, "total_power":{"$sum":"$power"}, "energy_dist":{"$addToSet": "$energy"}, "total_luminance": { "$avg": "$luminance"}}}]

def to_list(cursor):
       records = []
       for record in cursor:
               records.append(record)
       return records
