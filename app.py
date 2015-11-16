from flask import Flask, render_template, session, request, url_for, redirect, Markup
import yelp, google

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template("index.html")
    else:
        button = request.form['button']
        if button == "Set Location and Transit Method":
            prefTrans = request.form['transMethod']
            session['modeTrans'] = prefTrans
            userLocation = request.form['userLocation']
            session['userLocation'] = userLocation
            return render_template("index.html")
        elif button == "Search":
            food = request.form['food']
            if session.has_key('userLocation'):
                location = session['userLocation']
                return redirect ('/search/%s/%s' %(location,food))
            else:
                error = "Please set location and prefered method of transit"
                return render_template("index.html",error=error)
    return render_template("index.html")


@app.route("/search")
@app.route("/search/")
@app.route("/search/<location>/")
@app.route("/search/<location>/<term>")
def search(location="NY",term="restaurants"):
    restaurantDic = yelp.getRestaurants(term,location)
    return render_template("search.html",restaurants=restaurantDic)

@app.route("/directions")
def directions():
    start = session['userLocation']
    travelMethod = session['modeTrans']
    place = session['restaurantAddress']
    route1 = google.routeInstructions(start,place,travelMethod,0)
    route2 = google.routeInstructions(start,place,travelMethod,1)
    route3 = google.routeInstructions(start,place,travelMethod,2)
    theMap  = google.mapDirections(start,place,travelMethod)
    return render_template("directions.html",route1=route1,route2=route2, 
                           route3=route3,mapSrc = theMap)

@app.route("/redirectpage",methods=["GET","POST"])
def redirectpage():
    session['restaurantAddress'] = request.form['placeLocation']
    return redirect(url_for("directions"))

if __name__ == "__main__":
    app.debug = True
    app.secret_key="hoyinhoooo"
    app.run(host='0.0.0.0',port=8000)
