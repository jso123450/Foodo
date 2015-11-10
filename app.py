from flask
import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)
