import os
import sys
import time
import requests

#Define update URL's
url = "http://animal.georgevanburgh.co.uk:5000/update/RS0"

#Fetch and format the data
data = {'loadaverage': os.getloadavg()[0]}

if (requests.post(url, data).text == "200"):
  print "Update succeded!"
else:
  print "Update failed!"