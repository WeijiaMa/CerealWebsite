# datasource.py
# Created and edited by Ephraim Benson && Weijia Ma
# Last edited on October 25, 2017

import psycopg2
import psycopg2.extras # psycopg2.extras.DictCursor returns a dictionary object
from psycopg2 import sql
import getpass
import json # for formatted print output


# The file uses flask to handles the request from the front end
# and returns the relevant data obtained from the database.

class DataSource:
	# Connect to the database using user login info
	def __init__(self, database, user, password):
		try:
			self.connection = psycopg2.connect(database=database, user=user, password=password, cursor_factory=psycopg2.extras.DictCursor, host="localhost")
		except Exception as e:
			print('Connection error: ', e)
			exit()

	# Returns a string of sql query that selects cereals according to keywords and range filters
	def buildSQLQuery(self, rangeParamDict):
		# Build up the first part of the sql query string using keywords
		sqlCommand = "SELECT * FROM cereals WHERE UPPER(name) LIKE UPPER(%(keywordPlaceholder)s)"
		for param in rangeParamDict:
			minVal = rangeParamDict[param][0]
			maxVal = rangeParamDict[param][1]
			# Build up the second part of the sql query string for each parameter and its range values
			sqlCommand += " AND {} BETWEEN {} AND {}".format(param, minVal, maxVal)
		return sqlCommand

	# Returns an array of ceareals satisfying the search requirements.
	# Each entry of the array is a dictionary containing the detailed information of a cereal.
	def performSearch(self, keywords, rangeParamDict):
		sqlQuery = self.buildSQLQuery(rangeParamDict)
		try:
			cursor = self.connection.cursor()
			# run the sql query
			cursor.execute(sql.SQL(sqlQuery), dict(keywordPlaceholder = '%'+keywords+'%',))
			result = []
			for r in cursor.fetchall():
				result.append(dict(r))
			return result

		except Exception as e:
			print('Cursor error', e)
			self.connection.close()
			exit()