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
    
    Retrieves data from the yelp api given search parameters
    
    Args:
        url_params: (String) the part of a url that contains the what the user          wants to search

    Returns: 
        response: (Dictionary) contains all the information from yelp api   
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
    print(signed_url)
    conn = urllib2.urlopen(signed_url, None)
    response = json.loads(conn.read())
    conn.close()
    return response

def search(term, location):
    """

    Combines user inputs to create a url query

    Args:
        term: (String) Something to search for (e.g. restaurants, tacos)
        location: (String) In what location to search for.
    
    Returns:
        url: (String) Part of a url query that contains the  search parameters
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'radius_filter': RADIUS
    }
    url = request(url_params)
    return url

def getFullAddress(place):
    """

    Finds the full address of a restaurant given data from the yelp api

    Args:
        place: (Dictionary) contains information about a restaurant

    Returns:
        fulladdress: (String) the full address of the restaurant   

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
    
    Finds restaurants nearby the location specified with the specified food type    and returns the addresses and ratings

    Args:
       term: (String) The type of food desired
       location: (String) In what location to search for

    Returns:
       restaurants: (Dictionary) Name of the restaurants as keys and a list            containing the address and rating as the value
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

    Finds restaurants nearby the location given by the user that matches the        type of food given

    Args:
        term: The type of food desired
        location: The location to search for

    Returns:
        addresses: (Dictionary) A dictionary containing names of the restaurants        as keys and the addresses as values
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


