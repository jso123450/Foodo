import urllib2
import json

dKey = "AIzaSyCeavvXLPxaal8kb7SFnzYpShJ37vNCjQg"
mKey = "AIzaSyBSVLrtt6Hb6MDqyXdAHunxuYp0njyh2Dg"

def routes(start,end,mode):
    origin = start
    destination = end
    mode = mode
    baseurl = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=%s&alternatives=true&key=%s"
    url = baseurl % (origin, destination, mode, dKey)
    url = spaceRemover(url)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return r['routes']

def spaceRemover(url):
    return url.replace(" ","+")

#three routes to choose
def routeInstructions(start,end,mode,routeNum):
    result=""
    allRoutes = routes(start,end,mode)
    routeSteps = allRoutes[routeNum]['legs'][0]['steps']
    for step in routeSteps:
        result=result+step['html_instructions'].encode('utf8')+"<br>"
    return result

#note when returning this route
# long dash isn't properly returned. 
# returns questions marks. 
# something to do with the encoding


#use as source of iframe for use on website
def map(start,end,mode):
    origin = start
    destination = end
    mode = mode
    baseurl = "https://www.google.com/maps/embed/v1/directions?key=%s&origin=%s&destination=%s&mode=%s"
    url = baseurl % (mKey, origin, destination, mode)
    return url

#print map("Brooklyn+Bridge","Prospect+Park,Brooklyn","driving")
    
