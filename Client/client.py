import os
import time
import requests

#Define update URL's
url = "http://animal.georgevanburgh.co.uk:5000/update/RS0"

#Fetch and format the data
data = {'loadaverage': os.getloadavg()[0]}

print requests.post(url, data).text