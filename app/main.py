import cloudscraper
from flask import Flask
from flask import request

app = Flask(__name__) #sets the "app" variable to a Flask instance
scraper = cloudscraper.CloudScraper()


@app.route('/')
def mainR():
    return "OK"


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    print(request_data['url'])
    cookies = {'cf_clearance ': '04YmwuvvkkTSry5Ojo2Eu0Ci9eSOo9KiwxBeLTbR2U8-1636680056-0-150'}
    if request_data['get']:
      return scraper.get(request_data['url'] cookies=cookies).text
    else:
      headers = {'Content-Type': 'application/x-www-form-urlencoded'}
      return scraper.post(request_data['url'], headers=headers, data=request_data['data']).text
  
