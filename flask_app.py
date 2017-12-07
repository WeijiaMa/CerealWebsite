# flask_app.py
# Created and edited by Ephraim Benson && Weijia Ma
# Last edited on October 25, 2017

import flask
from flask import Flask, render_template, request
import json
import sys
from datasource import DataSource

# The file uses flask to handle the request from the front end
# and returns the relevant data obtained from the database.

# Connect to the database
database = "bensone"
user = "bensone"
password = "spam949books"
dataSource = DataSource(database, user, password)

app = Flask(__name__)

# Show the home page using template index.html
@app.route('/')
def showHomepage():
	return render_template('index.html')

# Show the about page using template about.html
# containing the biobliography and a short introduction of the website
@app.route('/about')
def showAbout():
	return render_template('about.html')

# Show the result page, handling HTTP requests
# User inputs such as keywords and range filters are obtained to perform a search in the database
@app.route('/result', methods = ['POST', 'GET'])
def showResults():
	if request.method == 'POST':
		cerealName = request.form['searchInput']
		min_calories = request.form['min-calories']
		max_calories = request.form['max-calories']
		min_sugars = request.form['min-sugars']
		max_sugars = request.form['max-sugars']
		min_protein = request.form['min-protein']
		max_protein = request.form['max-protein']
		min_rating = request.form['min-rating']
		max_rating = request.form['max-rating']

		paramDict = {"calories" : [min_calories, max_calories], "sugars" : [min_sugars, max_sugars], "protein" : [min_protein, max_protein], "rating" : [min_rating, max_rating]}
		# Handles the cases where useer has not input any value for the search filters
		for param in paramDict:
			if paramDict[param][0] == '':
				paramDict[param][0] = 0
			if paramDict[param][1] == '':
				paramDict[param][1] = 200

		searchResult = dataSource.performSearch(cerealName, paramDict)

		return render_template('result.html', result = searchResult)

# Connect to perlman host
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: {0} port'.format(sys.argv[0]), file=sys.stderr)
		exit()

	host = 'perlman.mathcs.carleton.edu'
	port = sys.argv[1]
	app.run(host=host, port=port)