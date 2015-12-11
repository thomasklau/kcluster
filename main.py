"""
Primary driver code for the kcluster pipeline.
"""

import sys
from tcga_tools import downloader, preprocessor
from kcluster import Clusterer

def print_help():
    print("""kCluster | version 0.0.1 | Bradbury, Lau, Roy

python main.py [help] [download] [preprocess] [kcluster]

help        -- print this help message
download    -- download files listed in tcga_files.json
preprocess  -- preprocess already downloaded files
kcluster    -- run the kcluster algorithm and display results

Submodules can be combined together to execute multiple
functions in a single call.""")

def main():
    argv = [a.lower() for a in sys.argv]

    if 'help' in argv:
        print_help()
        exit()
    if 'download' in argv:
        downloader.download('tcga_files.json')
        downloader.rename_all_data()
    if 'preprocess' in argv:
        preprocessor.process()
    if 'kcluster' in argv:
        kc = Clusterer('./data/processed.dat')
        kc.cluster()
        kc.display_2d()

if __name__ == '__main__': main()
