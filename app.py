from flask import Flask, Response
import requests
import json
import logging

app = Flask(__name__)



logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Verooo PRUEBA 2</p>"


@app.route("/get-price/<ticker>")
def get_price(ticker):
    url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    response = requests.get(url)
    result =response.json()
    print(result)

   


if __name__ == '__main__':
    app.run()


