from flask import Flask
from flask import render_template
from flask import request
from parseHTML import *
from glassdoor import *
import json
import requests
app = Flask(__name__, static_url_path="")

@app.route('/')
def root():
    getCompany('facebook')
    return render_template('main.html')
    #, schedule=getSchedule(), header=getHeaderInfo())

@app.route('/company')
def company():
    return render_template('company.html', logo=getLogo(request.args['name']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
