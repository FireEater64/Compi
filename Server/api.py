#Imports
import sys
sys.path.append('/modules')
from flask import Flask, jsonify, render_template, make_response, abort, request
from rrdtool import update as rrd_update
import json
import rrdmanage

#Load config
global computers = []
with open('file') as f:
    for line in f:
        computers.append(json.loads(line))

#Create app
app = Flask(__name__)

#Declare routes
@app.route("/", methods=['GET'])
def serveIndex():
    return render_template('index.html')

@app.route("/update/<computerName>", methods=['POST'])
def updateComputer(computerName):
    global computers

    #Check if computerName is valid
    if (not computerName in computers):
        return "404"

    #Update the RRD
    rrd_update(computerName + '.rrd', 'N:%s' %(average))
    #return computerName + ":\t" + str(request.form['loadaverage'])
    return "200"

#Handle errors
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

#Launch application
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
    #app.run()
