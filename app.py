import urllib
import json
import os
from flask import flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook',method=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    #print("Request:")
    #print(json.dumps(req,indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res,indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type']= 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != 'lunch':
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("lunch")
    speech = "급식은"+"낚지덮밥"
    #print("Respose:")
    #print(speech)
    return {
        "speech":speech,
        "displayText":speech,
        "source":"Bank"
    }

if __name__ == '__main__':
    #port  = int(os.getenv('POST',5000))
    app.run()
