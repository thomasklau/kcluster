import json
import os
import rpy2.robjects as robjects

with open('filenames.json') as data_file:
  filenames = json.load(data_file)

for dirname in filenames:
	for fname in os.listdir(dirname[0:-7]):
	  if fname.endswith(".txt") and "MANIFEST" not in fname:
	    print(fname)

robjects.r('''
        f <- function(r, verbose=FALSE) {
            if (verbose) {
                cat("I am calling f().\n")
            }
            2 * pi * r
        }
        f(3)
        ''')