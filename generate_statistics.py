#!/usr/bin/env python3

import json

with open('data/franken_data.json') as f:
	data = json.load(f)

examples = data['rasa_nlu_data']['common_examples']

intents = dict()
entities = dict()

intents_count = 0
entitites_count = 0
max_entities = 0
sum_len = 0
max_len_sentence = 0

for element in examples:
	if element['intent'] in intents:
		intents[element['intent']] += 1
	else:
		intents[element['intent']] = 1
	intents_count += 1
	sum_len += len(element['text'].split())
	if len(element['text'].split()) > max_len_sentence:
		max_len_sentence = len(element['text'].split())

	if 'entities' in element:
		if len(element['entities']) > max_entities:
			max_entities = len(element['entities'])

		for entity in element['entities']:
			if entity['entity'] not in entities:
				entities[entity['entity']] = {}
			entitites_count += 1
			if entity['value'] not in entities[entity['entity']]:
				entities[entity['entity']][entity['value']] = 1
			else:
				entities[entity['entity']][entity['value']] += 1

with open('stats/intent_results.csv','w') as f:
	f.write("intent,count\n")
	for int in intents:
		f.write("%s,%s\n" % (int,intents[int]))

with open('stats/entities_results.csv','w') as f:
	f.write("entity,description,count\n")
	for ent in entities:
		for spec in entities[ent]:
			f.write("%s,%s,%s\n" % (ent,spec,entities[ent][spec]))

with open('stats/dataset.csv','w') as f:
	f.write('%s,%s,%s,%s\n' % ('name','cuisine','location','price'))
	for cuisine in entities['cuisine']:
		for location in entities['location']:
			for price in ['cheap','moderate','expensive']:
				f.write('%s,%s,%s,%s\n' % ("",cuisine,location,price))

entities2 = dict()
for entity in entities:
	tmp_sum = 0
	for spec in entities[entity]:
		tmp_sum += entities[entity][spec]
	entities2[entity] = tmp_sum

print("# NLU PART #\n")

print("Entities type number: ")
for key in entities2:
	print("\t- %s: %d" % (key,entities2[key]))
print()

print("Examples number: %d" % intents_count)
print("Total entities: %d" % entitites_count)
print("Max number of entities: %d" % max_entities)
print("Max sentence len: %d" % max_len_sentence)
print("Sentence average len: %f" % (sum_len/intents_count))

print("Done franken data analysis\n\n")

################################################################################
import re
from functools import reduce

prog_re = re.compile('^[a-zA-Z_]*')
prog_arg = re.compile('{["a-zA-Z,: ]*}')

def get_data(text):
	return (prog_re.search(text)[0], prog_arg.search(text)[0] if prog_arg.search(text) is not None else {})

babi = open('data/babi_stories.md')

stories = []
story = []
for line in babi:

	line = line.strip()

	if line == "" or line.startswith('##'):
		if len(story) > 0:
			stories.append(story)
			story = []
		continue
	else:
		res = {}
		res['type'] = 'user' if line.startswith('*') else 'bot'
		res['move'], res['data'] = get_data(line.replace('*','').replace('-','').strip())
		story.append(res)

print("# DIALOGUE PART #\n")

print("Number of stories: %d" % len(stories))
print("Average stories length: %f" % (reduce((lambda x,y: x+y),(list(map(lambda x: len(x),stories)) ))/len(stories)))
statistics = {}
for story in stories:
	index = 1
	for move in story:
