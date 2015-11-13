import json
import urllib
import urllib2
import oauth2

RADIUS = 1000
CONSUMER_KEY = "nN_1rvj62gHje5i84nru4w"
CONSUMER_SECRET = "QgA2n5nULXrSDX_F2H5Hh_qRmUg"
TOKEN = "ucuSoWsDWPZFGzJzOR13g5GT53tUTR9g"
TOKEN_SECRET = "k399NqU0z3aelLkdhvM-8BEHyXQ"

def setRadius(limit):
    """ Sets RADIUS to limit.
    
    Limits the radius around the specified location that Yelp will search.

    Args:
        limit: (Integer) The distance one wants to search for a business.
    
    Returns:
        None.
    """
    RADIUS = limit

def request(url_params):
    """

    Args:


    Returns:
    
    """

    url = "https://api.yelp.com/v2/search/"
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)
    oauth_request["oauth_nonce"] = oauth2.generate_nonce()
    oauth_request["oauth_timestamp"] = oauth2.generate_timestamp()
    oauth_request["oauth_token"] = TOKEN
    oauth_request["oauth_consumer_key"] = CONSUMER_KEY

    token = oauth2.Token(TOKEN,TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    conn = urllib2.urlopen(signed_url, None)
    response = json.loads(conn.read())
    conn.close()
    return response

def search(term, location):
    """

    Args:
        term: (String) Something to search for (e.g. restaurants, tacos)
        location: (String) In what location to search for.
    
    Returns:

    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'radius_filter': RADIUS
    }
    return request(url_params)

def getFullAddress(place):
    """

    Args:
        place: (String) 

    """

    fulladdress = ""
    if (len(place["location"]["display_address"]) > 1):
        fulladdress = str(place["location"]["display_address"][0]) + " "
        if (len(place["location"]["display_address"]) == 3):
            fulladdress+= str(place["location"]["display_address"][2])
        else:
            fulladdress+= str(place["location"]["display_address"][1])
    return fulladdress

def getRestaurants(term, location):
    """

    Args:
       term: (String)
       location: (String)

    Returns:

    """

    restaurants = {}
    try:
        businesses = search(term, location)["businesses"]
        for place in businesses:
            fulladdress = getFullAddress(place)
            restaurants[str(place["name"])] = [fulladdress, place["rating"]]
    except:
        restaurants = {}
    return restaurants

def getAddresses(term, location):
    """

    Args:
        term:
        location:

    Returns:

    """
    addresses = {}
    try:
        businesses = search(term, location)["businesses"]
        for place in businesses:
            fulladdress = getFullAddress(place)
            addresses[str(place["name"])] = fulladdress
    except:
        addresses = {}
    return addresses


