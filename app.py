from flask import Flask,request,jsonify
import requests
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)

@app.route('/get_location')
@cache.cached(timeout=30, query_string=True)
def get_location():
    location_data = request.args.get('location_data')
    return {'message': 'Api success'}


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)