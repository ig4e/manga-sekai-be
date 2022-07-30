import cloudscraper
from flask import Flask
from flask import request
from flask_compress import Compress

app = Flask(__name__) #sets the "app" variable to a Flask instance111111
Compress(app)
scraper = cloudscraper.CloudScraper()

@app.route('/')
def mainR():
    return "OK"


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    if request_data['get']:
      return scraper.get(request_data['url']).text
    else:
      headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-requested-with': 'XMLHttpRequest' }
      return scraper.post(request_data['url'], headers=headers, data=request_data['data']).text
  
