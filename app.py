from flask import Flask, render_template
import requests as req
import json



app = Flask(__name__)


@app.route("/")
def home():
    resp=req.get("https://covid2019-api.herokuapp.com/total")

    p=resp.json()

    total_confirmed=[]
    total_deaths=[]
    total_recovered=[]
    date=[]
    for key,value in p.items():
        if(key=="confirmed"):
            total_confirmed.append(value)
        elif(key=="deaths"):
            total_deaths.append(value)
        elif(key=="recovered"):
            total_recovered.append(value)
        elif(key=="dt"):
            date.append(value)
    my_dict={"Coronavirus Cases":total_confirmed[0],"Deaths":total_deaths[0],"Recovered":total_recovered[0],"date":date[0]}


    #print(p)



    return render_template('index.html',list_to_send=my_dict)

if __name__ == "__main__":
    app.run(debug = True)