import urllib2
import json

dKey = "AIzaSyCeavvXLPxaal8kb7SFnzYpShJ37vNCjQg"
mKey = "AIzaSyBSVLrtt6Hb6MDqyXdAHunxuYp0njyh2Dg"

def routes(start,end,mode):
    """ Retrieves routes from the Google Maps Directions API.

    Args:
        start: Starting location.
        end: Destination.
        mode: method of transit

    Returns:
        

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
    return r['routes']

def spaceRemover(url):
    """ Removes spaces in a string.

    Args:

    Returns:

    """
    return url.replace(" ","+")

def routeInstructions(start,end,mode,routeNum):
    """ Returns the instructions in a route.

    Args:

    Return:

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

    Returns:


    """
    origin = start
    destination = end
    mode = mode
    baseurl = "https://www.google.com/maps/embed/v1/directions?key=%s&origin=%s&destination=%s&mode=%s"
    url = baseurl % (mKey, origin, destination, mode)
    return spaceRemover(url)

