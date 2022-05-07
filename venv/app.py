from flask import Flask,request,jsonify
import requests

app = Flask(__name__)


@app.route('/get_location')
def get_location():
    location_data = request.args.get('location_data')
    return {'message': 'Api success'}


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0",posty=5000)