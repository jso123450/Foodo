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
            if session.has_key('userLocation'):
                if session['userLocation']=="":
                    error="No location given"
                    return render_template("index.html",error=error)
                food = request.form['food']
                if food=="":
                    error="You're not craving anything."
                    return render_template("index.html",error=error)
                location = session['userLocation']
                return redirect ('/search/%s/%s' %(location,food))
            else:
                error = "Please set location and prefered method of transit"
                return render_template("index.html",error=error)
    return render_template("index.html")


@app.route("/search",methods=['GET','POST'])
@app.route("/search/",methods=['GET','POST'])
@app.route("/search/<location>/",methods=['GET','POST'])
@app.route("/search/<location>/<term>",methods=['GET','POST'])
def search(location="NY",term="restaurants"):
    if request.method=='GET':
        restaurantDic = yelp.getRestaurants(term,location)
        return render_template("search.html",restaurants=restaurantDic)
    else:
        return redirect(url_for(directions(request.form['placeName'])))

@app.route("/directions",methods=['GET','POST'])
def directions():
    session['restaurantAddress'] = request.form['placeLocation']
    start = session['userLocation']
    travelMethod = session['modeTrans']
    place = session['restaurantAddress']
    route1 = google.routeInstructions(start,place,travelMethod,0)
    try:
        route2 = google.routeInstructions(start,place,travelMethod,1)
    except:
        route2="No alternative"
    try:
        route3 = google.routeInstructions(start,place,travelMethod,1)
    except:
        route3 ="No alternative"
        
    theMap  = google.mapDirections(start,place,travelMethod)
    return render_template("directions.html",route1=route1,route2=route2, 
                           route3=route3,mapSrc = theMap)

if __name__ == "__main__":
    app.debug = True
    app.secret_key="hoyinhoooo"
    app.run(host='0.0.0.0',port=8000)
