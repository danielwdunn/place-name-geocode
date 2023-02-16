# Python program to get the latitude and longitude of a place based on its name. This may only work for unique and popular destinations. 

import requests
import time
import csv
from pandas import read_csv

# Use unique Google API key below. Keys can be generated from Google Cloud Console: https://console.cloud.google.com/
api_key = 'YOUR_API_KEY_HERE'
# Places URL
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# Input File
inputFile = 'endowmentList_source.csv'
# Output File
outputFile = 'endowmentList_Geocoded.csv'

# Read from CSV
data = read_csv(inputFile)
addresses = data['ConcatenatedAddress'].tolist()

for a in addresses:
    time.sleep(5)
    try:
    # The place string to search
        query = a
        r = requests.get(url + 'query=' + query + '&key=' + api_key)
        x = r.json()
        y = x['results']
        c1 = y[0]['geometry']['location']['lat']
        c2 = y[0]['geometry']['location']['lng']
        c3 = a
        with open(outputFile, mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow([c1, c2, c3])
    except:
        with open(outputFile, mode='a', newline='') as results_file:
            results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            results_writer.writerow(['error', 'error', a])


