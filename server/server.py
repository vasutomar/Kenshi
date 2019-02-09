from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
   return 'This is the obsidian server'

@app.route('/ret',methods=['GET'])
def my_file():

	d = {}
	with open('hack.json') as file:
		d = json.load(file)

	
	return jsonify(d) 



if __name__ == '__main__':
   app.debug = False
   app.run(host= '0.0.0.0', port="5000")