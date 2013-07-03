#Imports
from flask import Flask, jsonify, render_template, make_response, abort
#from flask import make_response
#from flask import abort
from pymongo import MongoClient

#Connect to database
client = MongoClient()
db = client.compstat
computers = db.computers
usersdb = db.users

#Create app
app = Flask(__name__)

#Declare routes
@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/computers", methods=['GET'])
def getComputers():
    toReturn = dict()
    computerInfo = computers.find()
    #Strip ObjectID's
    for computer in computerInfo:
        del computer["_id"]
        if ("Users" in computer):
            for user in computer["Users"]:
                 del user["_id"]
        toReturn[computer["Name"]] = computer
    return make_response(jsonify(toReturn))

@app.route("/computers/<computerName>", methods=['GET'])
def getComputer(computerName):
    #Check the requested computer exists
    if (computers.find({"Name": computerName}).count() == 0):
         abort(404)
    #Get the computer info
    computerInfo = computers.find_one({"Name": computerName})
    #Strip ObjectID's
    del computerInfo["_id"]
    if ("Users" in computerInfo):
        for users in computerInfo["Users"]:
            del users["_id"]
    return make_response(jsonify(computerInfo))

@app.route("/users/<userName>", methods=['GET'])
def getUsers(userName):
    #Return information about the given user name)
    user = dict()
    sessions = []
    user["Name"] = userName
    #Get all the users sessions
    rawSessions = computers.find({"Users.Name":userName})
    for session in rawSessions:
        sessions.append(session["Name"])
    user["Sessions"] = sorted(sessions)
    return make_response(jsonify(user))

@app.route("/lab", methods=['GET'])
def getLabDescription():
    #Return a list of valid labs
    toReturn = dict()
    labs = ["Toothill1","Toothill2","G23","LF31", "1.8", "2.25a", "2.25b", "2.25c"]
    toReturn["Labs"] = labs
    return make_response(jsonify(toReturn))

@app.route("/lab/<labName>", methods=['GET'])
def getLabInfo(labName):
    #Return informaton about the given lab
    return "Information about " + labName + "."

#Handle errors
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

#Launch application
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
    #app.run()
