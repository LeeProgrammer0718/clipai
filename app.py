import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify

app = Flask(__name__)
log = app.logger

@app.route('/webhook',methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    '''try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return log.error('error')'''
    #print("Request:")
    #print(json.dumps(req,indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res,indent=4)
    #res = action
    #print(res)
    r = make_response(res)
    #r = make_response(jsonify({'fulfillmentText': res}))
    r.headers['Content-Type']= 'application/json'
    return 'test'

def makeWebhookResult(req):
    if req.get("result").get("action") != 'lunch':
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("lunch")
    speech = "급식은 낚지덮밥"
    #print("Respose:")
    #print(speech)
    return {
        "speech":speech,
        "displayText":speech,
        "source":"heroku-clipai"
    }

if __name__ == '__main__':
    #port  = int(os.getenv('POST',5000))
    app.run(debug=True,host = '0.0.0.0')
