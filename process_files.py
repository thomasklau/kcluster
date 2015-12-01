import json
import os

with open('filenames.json') as data_file:
  filenames = json.load(data_file)

for dirname in filenames:
	for fname in os.listdir(dirname[0:-7]):
	  if fname.endswith(".txt") and "MANIFEST" not in fname:
	    print(fname)
