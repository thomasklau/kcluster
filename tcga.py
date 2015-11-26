# See https://confluence.broadinstitute.org/display/GDAC/fbget#main-content.wiki-content
# Also see http://firebrowse.org/api-docs/
import firebrowse

# example query of fbget on EGFR's mRNAseq information in UCS cohort
print  firebrowse.Samples().mRNASeq(gene="egfr", cohort="ucs")

# we can additionally get this data in JSON format
# 