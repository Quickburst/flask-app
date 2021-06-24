from flask import Flask
app = Flask(__name__)

@app.route("/RESTfulExample/json/product/get")
def hello():
    return "Hello !!"

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port = 5000)