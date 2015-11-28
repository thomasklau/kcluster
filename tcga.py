# See https://confluence.broadinstitute.org/display/GDAC/fbget#main-content.wiki-content
# Also see http://firebrowse.org/api-docs/
import json
import firebrowse

# example query of firebrowse on EGFR's mRNAseq information in UCS cohort
# firebrowse.Samples().mRNASeq(gene="egfr", cohort="ucs", format="json")

datatypes = ["CopyNumber","RPPA","mRNA","miRNA","Methylation"]

dates = "2015_08_21,2015_06_01,2015_04_02,2015_02_04,2014_12_06,2014_10_17,2014_09_02,2014_07_15,2014_05_18,2014_04_16,2014_03_16"

text = firebrowse.Archives().StandardData(cohort="brca", date=dates, data_type=datatypes[0], page="1", page_size="2000")

data = json.loads(text)

print data['StandardData'][0]['urls'][0]

f = open('data.json', 'w')
f.write(text)
f.close()