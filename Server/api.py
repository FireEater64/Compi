#Imports
from flask import Flask, jsonify, render_template, make_response, abort, request
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
def serveIndex():
    return render_template('index.html')

@app.route("/update/<computerName>", methods=['POST'])
def updateComputer(computerName):
    return computerName + ":\t" + str(request.form['loadaverage'])

#Handle errors
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

#Launch application
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
    #app.run()
