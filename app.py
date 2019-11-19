#Joseph Yusufov, Mudadour Rahman, Alice Ni, David Wang
#SoftDev1 pd2
#Atmosphere
#2019-11-xx

from flask import Flask, render_template, request, session
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import flash
from flask import url_for
import urllib
import json
import random
import csv
import sqlite3
import os

# m49 = {}
# reader = csv.reader(open("./data/M49.csv", "r"))
# for row in reader:
    # print(row)
    # m49[row[0]] = row[1]

# print(m49)

app = Flask(__name__)  # create instance of class Flask
app.secret_key = os.urandom(24)


@app.route("/")  # assign following fxn to run when root route requested
def index():
    return render_template('index.html')



@app.route("/login")
def login():
	if "username" in request.args:
		// sqlite check
	else:
		return render_template("login.html")
	return "reee"



@app.route("/lookup")
def lookup():
    if 'user' in session:
        if request.args:
            r = urllib.request.urlopen(
                "" # Some API link goes here
            )
            data = json.loads(r.read())
            data = data['data'][0]
            print(data)
            # print(data['results'][0]['name'])
            return render_template("lookup.html", data=data)

        else:
            r = urllib.request.urlopen(
                "" # Some API link goes here
            )
            data = json.loads(r.read())
            data = data['data'][0]
            print(data);
            # print(data['results'][0]['name'])
            return render_template("lookup.html", data=data)




if __name__ == "__main__":
    app.debug = True
    app.run()
