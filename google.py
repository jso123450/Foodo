import urllib2
import json

dKey="AIzaSyCeavvXLPxaal8kb7SFnzYpShJ37vNCjQg"
mKey="AIzaSyBSVLrtt6Hb6MDqyXdAHunxuYp0njyh2Dg"
def directions(start,end,mode):
    origin = start
    destination = end
    mode = mode
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=%s&key=%s" %(origin, destination, mode, dKey)
    print url
    request = urllib2.urlopen(url)
    result = request.read()
    r=json.loads(result)
    print r.keys()
    step0= r['routes'][0]['legs'][0]['steps'][0]
    print step0['html_instructions']
#print directions("Brooklyn_Bridge","Prospect_Park,Brooklyn","driving")

#use as source of iframe for use on website
def map(start,end,mode):
    origin = start
    destination = end
    mode = mode
    url="https://www.google.com/maps/embed/v1/directions?key=%s&origin=%s&destination=%s&mode=%s" %(mKey, origin, destination, mode)
    return url

print map("Brooklyn_Bridge","Prospect_Park,Brooklyn","driving")
    
