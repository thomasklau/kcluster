# See https://confluence.broadinstitute.org/display/GDAC/fbget#main-content.wiki-content
# Also see http://firebrowse.org/api-docs/
import firebrowse
import json
import re
import download
import tarfile

text = firebrowse.Archives().StandardData(cohort="brca", date='2015_06_01', data_type='CopyNumber,RPPA,Methylation', page="1", page_size="2000")

data = json.loads(text)

# f1 = open('data.json', 'w')
# f1.write(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
# f1.close()


def includeObj(obj):
	if obj["sample_prep"] == "ffpe":
		return False
	elif obj["data_type"] == "Methylation" and ("platform" not in obj or obj["platform"] == "humanmethylation450"):
		return False
	else:
		return True

data["StandardData"] = [obj for obj in data["StandardData"] if includeObj(obj)]

# f2 = open('data.json', 'w')
# f2.write(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
# f2.close()

def includeURL(url):
	if re.search("Level_3\.[0-9]{10}\.0\.0\.tar.gz$", url):
		return True
	else:
		return False

for i in range(len(data["StandardData"])):
	data["StandardData"][i]["urls"] = [url for url in data["StandardData"][i]["urls"] if includeURL(url)]

# f3 = open('data.json', 'w')
# f3.write(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
# f3.close()

filenames = []
for obj in data["StandardData"]:
	fname = obj["urls"][0].split('/')[-1]
	# UNCOMMENT THIS TO DOWNLOAD FILES
	# download.downloadFile(obj["urls"][0], fname)
	filenames.append(fname)

def untar(fname):
  if (fname.endswith("tar.gz")):
      tar = tarfile.open(fname)
      tar.extractall()
      tar.close()

# UNCOMMENT THIS TO UNZIP FILES
# for name in filenames:
	# untar(name)

f4 = open('filenames.json', 'w')
f4.write(json.dumps(filenames, indent=2, separators=(',', ': ')))
f4.close()