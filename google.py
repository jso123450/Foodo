import urllib2
import json

dKey = "AIzaSyCeavvXLPxaal8kb7SFnzYpShJ37vNCjQg"
mKey = "AIzaSyBSVLrtt6Hb6MDqyXdAHunxuYp0njyh2Dg"

def spaceRemover(url):
    """ Removes spaces in a string.

    Args:
        url: (string) string with spaces
    Returns:
        result: (string) url with spaces replaced with +
    """
    result=url.replace(" ","+")
    return result

def routes(start,end,mode):
    """ Retrieves routes from the Google Maps Directions API.

    Args:
        start: (string)Starting location.
        end: (string) Destination.
        mode: (string) method of transit

    Returns:
        routes: (array) An array of the routes. Each route is a array with
        steps of the directions inside.

    """
    origin = start
    destination = end
    mode = mode
    baseurl = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=%s&alternatives=true&key=%s"
    url = baseurl % (origin, destination, mode, dKey)
    url = spaceRemover(url)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    routes=r['routes']
    return routes

print routes("New+York","Stuyvesant+High+School","driving")

def routeInstructions(start,end,mode,routeNum):
    """ Returns the instructions in a route.

    Args:
        start: (string)Starting location.
        end: (string) Destination.
        mode: (string) method of transit
        routeNum: (int) route number
    Return:
        result: (string) html with all the steps for that route. 
        Each step on seperate line.

    """
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


def mapDirections(start,end,mode):
    """ Returns a map from Google Maps Embed API.

    Args: 
        start: (string)Starting location.
        end: (string) Destination.
        mode: (string) method of transit

    Returns:
        url: (string) url of the embedded map that will be used as source
        of a iFrame in html

    """
    origin = start
    destination = end
    mode = mode
    baseurl = "https://www.google.com/maps/embed/v1/directions?key=%s&origin=%s&destination=%s&mode=%s"
    url = baseurl % (mKey, origin, destination, mode)
    url = spaceRemover(url)
    return url

