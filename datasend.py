import json
import urllib.request
text = '테스트1234'
d = {'displayText':text}
params = json.dumps(d).encode("utf-8")
req = urllib.request.Request(url, data=params,
                             headers={'content-type': 'application/json'})
