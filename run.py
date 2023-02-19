from flask import Flask
from datetime import datetime
from pytz import timezone
app = Flask(__name__)

NYC_timezone = timezone('US/Eastern')

@app.route('/time')
def get_time():
    return datetime.now(NYC_timezone).strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def hello_world():
    return 'Hello world!'


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
