#!/usr/bin/env python

import os
import csv

base_dir = os.path.dirname(__file__) + '/..'

json = '{"name": "readers","children": ['

with open(base_dir + '/output/part-r-00000', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter='	')
	json += ','.join(map(lambda row: '{"name": "' + row[0] + '", "size": ' + row[1] + '}', reader))
	# {"name": "NAME", "size": 3938}

json += ']}'

with open(base_dir + '/public/data/top_readers.json', 'wb') as jsonfile:
	jsonfile.write(json)
