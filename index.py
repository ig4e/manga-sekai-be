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
    if request_data['get']:
      return scraper.get(request_data['url']).text
    else:
      headers = {'Content-Type': 'application/x-www-form-urlencoded'}
      return scraper.post(request_data['url'], headers=headers, data=request_data['data']).text
  
port = int(os.environ.get('PORT', 5000))
app.run('0.0.0.0', port=port)
