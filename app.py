from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",  methods=["GET"]) # GET POST PUT DELETE
def hello():
    return "Hello World!"

@app.route("/home",  methods=["GET"]) # GET POST PUT DELETE
def home():
    return render_template('index.html')

@app.route("/<name_of_page>",methods=["GET"])
def dynamic_route(name_of_page):
    return name_of_page.upper()

if __name__ == "__main__":
    app.run(host="0.0.0.0")		