from pymongo import MongoClient, database
import subprocess
import threading
import pymongo
from datetime import datetime, timedelta
import time

DBName = "Cluster0" #Use this to change which Database we're accessing
connectionURL = "mongodb+srv://josejimenez530:Cecs327@cluster0.16uku4k.mongodb.net/?retryWrites=true&w=majority" #Put your database URL here
sensorTable = "traffic data_metadata" #Change this to the name of your sensor data table

def QueryToList(query):
	l1 = []
	for x in query:
		l1.append(x)
	return l1
  #TODO: Convert the query that you get in this function to a list and return it
  #HINT: MongoDB queries are iterable
  #THINK I THIS PART

def QueryDatabase():
	global DBName
	global connectionURL
	global currentDBName
	global running
	global filterTime
	global sensorTable
	cluster = None
	client = None
	db = None
	try:
		cluster = connectionURL
		client = MongoClient(cluster)
		db = client[DBName]
		print("Database collections: ", db.list_collection_names())

		#We first ask the user which collection they'd like to draw from.
		sensorTable = db[sensorTable]
		print("Table:", sensorTable)
		#We convert the cursor that mongo gives us to a list for easier iteration.
		timeCutOff = datetime.now() - timedelta(minutes=0) #TODO: Set how many minutes you allow

		oldDocuments = QueryToList(sensorTable.find({"time":{"$gte":timeCutOff}}))
		currentDocuments = QueryToList(sensorTable.find({"time":{"$lte":timeCutOff}}))

		print("Current Docs:",currentDocuments)
		print("Old Docs:",oldDocuments)

		#TODO: Parse the documents that you get back for the sensor data that you need
		#Return that sensor data as a list
		data1 = []
		for x in currentDocuments:
			data1.append(x)
		return data1
		


	except Exception as e:
		print("Please make sure that this machine's IP has access to MongoDB.")
		print("Error:",e)
		exit(0)

