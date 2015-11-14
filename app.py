from flask import Flask, render_template, session
import yelp, google

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/search")
@app.route("/search/")
@app.route("/search/<location>/")
@app.route("/search/<location>/<term>")
def search(location="NY",term="restaurants"):
    restaurantDic = yelp.getRestaurants(term,location)
    return render_template("search.html",restaurants=restaurantDic)

@app.route("/directions/<place>/<travelMethod>")
def directions(place="",travelMethod=session['prefMode']):
    start = session['userLocation']
    route1 = google.routeInstructions(start,place,travelMethod,0)
    route2 = google.routeInstructions(start,place,travelMethod,1)
    route3 = google.routeInstructions(start,place,travelMethod,2)
    map  = google.map(start,place,travelMethod)
    return render_template("directions.html",route1=route1,route2=route2, 
                           route3=route3,mapSrc = map)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
