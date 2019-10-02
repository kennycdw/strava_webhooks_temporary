from flask import Flask, request, redirect, url_for, render_template, send_from_directory, Response
import requests
import json

client_id = ""
client_secret = ""
weblink = "domainname"
strava_webhook_url = "https://api.strava.com/api/v3/push_subscriptions"

app = Flask(__name__)



@app.route("/stravaresponse", methods = ['GET'])
def strava_response():
    if request.args.get('hub.mode') == 'subscribe':
        payload = {'hub.challenge': request.args['hub.challenge']}
        jsonpayload = json.dumps(payload)  # {"hub.challenge": "0f1b641969427f4b"}  << output generated
    return json.dumps(payload)

"""
I tried submitting a post request and got a 'non verifiable code'
r = requests.post(url = strava_webhook_url, data = {'client_id': client_id, "client_secret": client_secret, 'callback_url': f'{weblink}/stravaresponse',
                                                    'verify_token': 'STRAVA'})
                                                    
print(r.text)

{"message":"Bad Request","errors":[{"resource":"PushSubscription","field":"callback url","code":"not verifiable"}]}

"""

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
