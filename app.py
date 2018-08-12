import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import datetime
app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    '''try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return log.error('error')'''
    print("Request:")
    print(json.dumps(req,indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res,indent=4)
    #res = action
    print(res)
    r = make_response(res)
    #r = make_response(jsonify({'fulfillmentText': res}))
    r.headers['Content-Type']= 'application/json'
    return r

def lunchparse(date): 
    date = str(date)
    url = "http://pungduck.hs.kr/lunch.view?date="+"2018"+"08"+"14"
    r = requests.get(url)
    c = r.content
    html = BeautifulSoup(c,"html.parser") #html 파싱
    print(html)
    menu = html.find("div",{"class":"menuName"})
    print(menu)
    try:
        span = menu.find("span")
        print(span.text)
        return span.text#메뉴출력
    except:
           return "급식이 없어 "
        
def makeWebhookResult(req):
    if req.get("result").get("action") != 'lunch':
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("lunch")
    speech = lunchparse(14)
    print("Respose:")
    print(speech)
    return {
        "speech":speech,
        "displayText":speech,
        "source":"clipai"
    }

if __name__ == '__main__':
    port  = int(os.getenv('PORT',5000))
    print(port)
    app.run(debug=True,port=port,host = '0.0.0.0')
    #app.run()    
