#!/usr/bin/env python3
from pymongo import MongoClient
import csv

client = MongoClient('mongodb://localhost:27017/')
collection = client.jarvis.restaurants

# cleaning collecion
collection.remove()

with open('data/restaurants_dataset.csv') as f:
	spamreader = csv.reader(f,delimiter=';')
	"""name;cuisine;location;price"""
	for row in spamreader:
		tmp = dict()
		tmp['name'] = row[0]
		tmp['cuisine'] = row[1]
		tmp['location'] = row[2]
		tmp['price'] = row[3]

		collection.insert_one(tmp)

print("%d restaurants inserted" % len([x for x in collection.find()]))
