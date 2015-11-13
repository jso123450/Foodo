from flask import Flask, render_template
import yelp

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

@app.route("/location/<place>")
def location(place=""):
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
