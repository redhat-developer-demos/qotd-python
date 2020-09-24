import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

quotes = [
    {'id': 0,
     'quotation': 'It is not only what you do, but also the attitude you bring to it that makes you a success.',
     'author': 'Don Schenck'},
    {'id': 1,
     'quotation': 'Knowledge is power.',
     'author': 'Francis Bacon'},
    {'id': 2,
     'quotation': 'Life is really simple, but we insist on making it complicated.',
     'author': 'Confucius'},
    {'id': 3,
     'quotation': 'This above all, to thine own self be true.',
     'author': 'William Shakespeare'},
    {'id': 4,
     'quotation': 'I got a fever, and the only prescription is more cowbell.',
     'author': 'Will Ferrell'},
    {'id': 5,
     'quotation': 'Do be do be dooo.',
     'author': 'Frank Sinatra'}
]

@app.route('/', methods=['GET'])
def home():
    return "qotd"

@app.route('/version', methods=['GET'])
def version():
    return "2.0.0"

@app.route('/writtenin', methods=['GET'])
def writtenin():
    return "Python"

@app.route('/quotes', methods=['GET'])
def getQuotes():
    return jsonify(quotes)

@app.route('/quotes/<int:id>', methods=['GET'])
def getQuoteById(id):
    return jsonify(quotes[id])

@app.route('/quotes/random', methods=['GET'])
def getRandom():
    n = random.randint(0,5)
    return jsonify(quotes[n])

if __name__ == '__main__':
    app.run(host="localhost", port=10000)