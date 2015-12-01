# See https://confluence.broadinstitute.org/display/GDAC/fbget#main-content.wiki-content
# Also see http://firebrowse.org/api-docs/
import json
import firebrowse

# example query of firebrowse on EGFR's mRNAseq information in UCS cohort
# firebrowse.Samples().mRNASeq(gene="egfr", cohort="ucs", format="json")

datatypes = ["CopyNumber","RPPA","mRNA","miR","Methylation"]

text = firebrowse.Archives().StandardData(cohort="brca", date='2015_06_01', data_type='CopyNumber,RPPA,mRNA,miR,Methylation', page="1", page_size="2000")

data = json.loads(text)

f1 = open('data1.json', 'w')
f1.write(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
f1.close()

data["StandardData"] = [obj for obj in data["StandardData"] if not obj["sample_prep"] == "ffpe"]

f2 = open('data2.json', 'w')
f2.write(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
f2.close()