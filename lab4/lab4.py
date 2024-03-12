from flask import Flask, request, jsonify
from lab3 import parser

### Пожалейте бедолагу, не подавайте ему ничего, кроме "http://127.0.0.1:5000/parse?url=https://www.weatheronline.co.uk/Sweden/Enkoping.htm" ###
### Спасибо! ###
app = Flask(__name__)
@app.route('/parse', methods = ['GET'])

def parse_url():
    url = request.args.get('url')
    data = parser(url)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)