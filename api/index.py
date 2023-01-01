from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_cur(incur,outcur):
    url = f"https://www.x-rates.com/calculator/?from={incur}&to={outcur}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content,'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = rate[:-4]
    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello World</h1> <p>Example URL: /api/v1/usd-eur"

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur,out_cur):
    rate = get_cur(in_cur,out_cur)
    result_dict = {"input currency":in_cur,"output currency":out_cur,"rate":rate}
    return jsonify(result_dict)


app.run(host="localhost")