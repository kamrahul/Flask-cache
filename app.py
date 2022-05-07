from flask import Flask,request,jsonify
import requests
from flask_caching import Cache

app = Flask(__name__)
#app.config.from_object('config.Config')
#cache = Cache(app)
cache = Cache(app, config={'CACHE_TYPE': 'redis',
'CACHE_TYPE':'redis',
'CACHE_REDIS_HOST':'redis',
'CACHE_REDIS_PORT':'6379',
'CACHE_REDIS_DB':'0',
'CACHE_REDIS_URL':'redis://redis:6379/0',
'CACHE_DEFAULT_TIMEOUT':'500'})

print(app.config)

@app.route('/get_location')
@cache.cached(timeout=30, query_string=True)
def get_location():
    import time 
    time.sleep(100)
    location_data = request.args.get('location_data')
    return {'message': 'Api success'}


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
