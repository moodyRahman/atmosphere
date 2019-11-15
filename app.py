#Joseph Yusufov, Mudadour Rahman, Alice Ni, David Wang
#SoftDev1 pd2
#Atmosphere
#2019-11-xx

from flask import Flask, render_template, request
import urllib
import json
import random
import csv

m49 = {}
reader = csv.reader(open("./data/M49.csv", "r"))
for row in reader:
    # print(row)
    m49[row[0]] = row[1]

# print(m49)
app = Flask(__name__)  # create instance of class Flask


@app.route("/")  # assign following fxn to run when root route requested
def hello_world():
    return render_template("index.html")


@app.route("/lookup")
def lookup():
    if request.args:
        r = urllib.request.urlopen(
            "https://unstats.un.org/SDGAPI/v1/sdg/Indicator/Data?indicator=1.1.1&areaCode={}&timePeriod=2017&dimensions=%5B%7Bname%3A%22Age%22%2Cvalues%3A%5B%2215%2B%22%5D%7D%2C%20%7Bname%3A%22Sex%22%2Cvalues%3A%5B%22BOTHSEX%22%5D%7D%5D".format(m49[request.args.get('country')])
        )
        data = json.loads(r.read())
        data = data['data'][0]
        print(data)
        # print(data['results'][0]['name'])
        return render_template("lookup.html", data=data, countries=m49.keys())

    else:
        r = urllib.request.urlopen(
            "https://unstats.un.org/SDGAPI/v1/sdg/Indicator/Data?indicator=1.1.1&areaCode=1&timePeriod=2017&dimensions=%5B%7Bname%3A%22Age%22%2Cvalues%3A%5B%2215%2B%22%5D%7D%2C%20%7Bname%3A%22Sex%22%2Cvalues%3A%5B%22BOTHSEX%22%5D%7D%5D"
        )
        data = json.loads(r.read())
        data = data['data'][0]
        print(data);
        # print(data['results'][0]['name'])
        return render_template("lookup.html", data=data, countries=m49.keys())



if __name__ == "__main__":
    app.debug = True
    app.run()
