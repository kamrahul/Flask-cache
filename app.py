from ast import arg
from http import server
from flask import Flask,request,jsonify
import requests
from flask_caching import Cache
import json

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'redis',
'CACHE_TYPE':'redis',
'CACHE_REDIS_HOST':'redis',
'CACHE_REDIS_PORT':'6379',
'CACHE_REDIS_DB':'0',
'CACHE_REDIS_URL':'redis://redis:6379/0',
'CACHE_DEFAULT_TIMEOUT':'500'})

print(app.config)

@app.route('/get_address/<string:latitude>/<string:longitude>')
@cache.cached(timeout=(24*60*60), query_string=True)
def get_address(latitude,longitude):

    #Base URL for address service
    URL = 'https://nominatim.openstreetmap.org/reverse'

    #Variables for final response
    final_response={}
    status_code=200
    location_data=''

    # Get request params
    mock_test = False
    args = request.args

    # if mock is present do not send request to server for addres
    if args.get("mock") :
        mock_test = True
    try:
        # sending get request and saving the response as response object
        if not mock_test :
            location_data = requests.get(url = URL, params = {'format':'jsonv2','lat':latitude,'lon':longitude})
        else:
            return {'lookup':'CACHE'},202
    except requests.exceptions.RequestException as e:
        # IF issue with request
        return {'error':"API request failed . Please retry"},503 # retry status

    # Converting byte object to Json
    #location_data = json.loads(location_data.content.decode('utf-8'))
    location_data = location_data.json()


    if('error' in location_data):
        # If there is no data found
        final_response ={'error':'Cannot find details'}
        status_code=404 # Not found status
    else:
        final_response={'name':location_data.get('display_name')}
   
    return final_response,status_code


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
