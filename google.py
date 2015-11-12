import urllib2
import json

key="AIzaSyCeavvXLPxaal8kb7SFnzYpShJ37vNCjQg"

def directions(start,end,mode):
    origin = start
    destination = end
    mode = mode
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=%s&key=%s" %(origin, destination, mode, key)
    print url
    request = urllib2.urlopen(url)
    result = request.read()
    r=json.loads(result)
    print r.keys()
    step0= r['routes'][0]['legs'][0]['steps'][0]
    print step0['html_instructions']
print directions("Brooklyn_Bridge","Prospect_Park,Brooklyn","driving")
