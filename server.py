#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

stats= { 
    'kills': {'22/03/2019': 20, '23/03/2019':2, '24/03/2019':0}, 
    'damages': {'22/03/2019': 2523, '23/03/2019':600, '24/03/2019':53}, 
    'top1': {'22/03/2019': 0, '23/03/2019': 3, '24/03/2019': 1}
    }

@app.route('/statistiques')
def home():
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)