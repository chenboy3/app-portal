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
    tup = getLogo(request.args['company'])
    if tup == None:
        print('not found')
        return render_template('main.html')
    else:
        #del logo[1]['featuredReview']
        #print(json.dumps(logo[1], indent=4, sort_keys=True))
        return render_template('company.html',
            logo=tup[0], name=tup[1], site=tup[2], rating=tup[3], industry=tup[4])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
