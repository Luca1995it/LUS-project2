from pymongo import MongoClient

class RestaurantAPI(object):
	def __init__(self):
		client = MongoClient('mongodb://localhost:27017/')
		self.db = client.jarvis

	def db_query(self, query):
		return [x for x in self.db.restaurants.find(query)]

	def search(self, query):
		res = self.db_query(query)
		if len(res) > 0:
			return res
		if 'location' in query:
			del query['location']
		res = self.db_query(query)
		if len(res) > 0:
			return res
		if 'price' in query:
			del query['price']
		res = self.db_query(query)
		if len(res) > 0:
			return res
		if 'cuisine' in query:
			del query['cuisine']
		res = self.db_query(query)
		return res
