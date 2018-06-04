#!/usr/bin/env python
from random import shuffle

TRAIN_PERCENTAGE = 0.7

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
		story.append(line)

with open('data/train_babi_stories.md','w') as train, open('data/evaluate_babi_stories.md','w') as eval:
	split_point = int(len(stories)*TRAIN_PERCENTAGE)
	count = 1
	shuffle(stories)
	for story in stories:
		if count < split_point:
			target = train
		else:
			target = eval
		target.write("## %d" % count)
		for s in story:
			if s.strip().startswith("-"):
				target.write(" %s" % s)
			else:
				target.write(s)
			target.write('\n')
		target.write('\n')
		count += 1
