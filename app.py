from flask import Flask, render_template
import requests as req
import json



app = Flask(__name__)


@app.route("/")
def home():

    #print(p)



    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)
