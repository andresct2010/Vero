from flask import Flask, Response
import requests
import json
import logging

app = Flask(__name__)



logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Verooo PRUEBA 3</p>"


@app.route("/get-price")
def get_price():
    url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/MSFT?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    response = requests.get(url)
    result =response.json()
    print(result)

@app.route("/price")
def price():   
    url = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/MSFT?modules=price%2CsummaryDetail%2CpageViews%2CfinancialsTemplate"
    r = requests.get(url)
    result =r.json()
    price = result['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']

    return ("<p>"+ price+"</p>")
    


if __name__ == '__main__':
    app.run()


