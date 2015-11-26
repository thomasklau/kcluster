# See https://confluence.broadinstitute.org/display/GDAC/fbget#main-content.wiki-content
# Also see http://firebrowse.org/api-docs/
import fbget

# example query of fbget on EGFR's mRNAseq information in UCS cohort
print fbget.mrnaseq("egfr", cohort="ucs", format = "json")

# we can additionally get this data in JSON format
# 