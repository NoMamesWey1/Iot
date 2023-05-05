from pymongo import MongoClient, database
import subprocess
import threading
import pymongo
from datetime import datetime, timedelta
import time
import certifi

DBName = "test"  # Use this to change which Database we're accessing
connectionURL = "mongodb+srv://josejimenez530:cecs327@cluster0.bojal4q.mongodb.net/?retryWrites=true&w=majority"  # Put your database URL here
sensorTable = "traffic data"  # Change this to the name of your sensor data table


def QueryToList(query):
    result = []
    for x in query:
        result.append(x)
    return result
        
# TODO: Convert the query that you get in this function to a list and return it
# HINT: MongoDB queries are iterable
# THINK I THIS PART

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
        client = MongoClient(cluster,tlsCAFile=certifi.where())
        db = client[DBName]
        print("Database collections: ", db.list_collection_names())

        # We first ask the user which collection they'd like to draw from.
        sensorTable = db[sensorTable]
        print("Table:", sensorTable)
        # We convert the cursor that mongo gives us to a list for easier iteration.
        timeCutOff = datetime.now() - timedelta(minutes=5)  # TODO: Set how many minutes you allow

        oldDocuments = QueryToList(sensorTable.find({"time": {"$gte": timeCutOff}}))
        currentDocuments = QueryToList(sensorTable.find({"time": {"$lte": timeCutOff}}))

        print("Current Docs:", currentDocuments)
        print("Old Docs:", oldDocuments)

        # TODO: Parse the documents that you get back for the sensor data that you need
        # Return that sensor data as a list
        oldSensorData = []
        for doc in (oldDocuments):
            data = {
                "Roads": doc["payload"],
            }
            oldSensorData.append(data)

        currentSensorData = []
        for doc in (currentDocuments):
            data = {
                "Roads": doc["payload"],
            }
            currentSensorData.append(data)
        length = len(oldSensorData)//2
        roadA = (oldSensorData[length+0]["Roads"]["TRAFFIC SENSOR"] + oldSensorData[length+3]["Roads"]["TRAFFIC SENSOR"]) // 2
        roadB = (oldSensorData[length+1]["Roads"]["TRAFFIC SENSOR"] + oldSensorData[length+4]["Roads"]["TRAFFIC SENSOR"]) // 2
        roadC = (oldSensorData[length+2]["Roads"]["TRAFFIC SENSOR"] + oldSensorData[length+5]["Roads"]["TRAFFIC SENSOR"]) // 2
        print("made it")
        roada = oldSensorData[length+0]["Roads"]["topic"]
        roada = roada[12:17]
        roadb = oldSensorData[length+1]["Roads"]["topic"]
        roadb = roadb[12:17]
        roadc = oldSensorData[length+2]["Roads"]["topic"]
        roadc = roadc[12:17]
        ans = min(roadA, min(roadC, roadB))
        ans = str(ans)
        if ans == roadA:
            ans = oldSensorData[0]["Roads"]["topic"]
        elif ans == roadB:
            ans = oldSensorData[1]["Roads"]["topic"]
        else:
            ans = oldSensorData[2]["Roads"]["topic"]
        print(f"\nAvg for {roada} is {roadA}\nAvg for {roadb} is {roadB}\nAvg for {roadc} is {roadC}\nBest avg road is {ans[12:17]}")
        return ans



    except Exception as e:
        print("Please make sure that this machine's IP has access to MongoDB.")
        print("Error:", e)
        exit(0)
