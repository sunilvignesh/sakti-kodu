def streets_pipeline(street_name):
	return [{"$match":{"street":street_name}},{"$group":{"_id":"street","total":{"$sum":1},"energy_dist":{"$addToSet": "$energy"}}}, { "$project" : {
        "streetlights" : "$total" ,
        "total_energry" : "$energy" ,
        "total_power" : "$power",
        "energy_dist" : "$energy_dist"
    }}]
