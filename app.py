from flask import Flask, Response
import requests
import json
import logging

app = Flask(__name__)



logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Verooo PRUEBA 3</p>"


@app.route("/price/<ticker>")
def price(ticker : str):   
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey=demo"
    r = requests.get(url)
    result =r.json()
    return result


@app.route("/moneda/<ticker>")
def moneda(ticker : str):   
    url = f"https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol={ticker}&to_symbol=USD&interval=5min&apikey=demo"
    r = requests.get(url)
    result =r.json()
    return result
    


if __name__ == '__main__':
    app.run()


