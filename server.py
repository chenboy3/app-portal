from flask import Flask
from flask import render_template
from parseHTML import *
import json
app = Flask(__name__, static_url_path="")

@app.route('/')
def root():
    return render_template('main.html', schedule=getSchedule())

@app.route('/classes')
def classes():
    return json.dumps(getClasses())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
