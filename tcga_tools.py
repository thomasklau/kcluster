"""
Helpful tools for downloading and processing TCGA data from The Broad Institute.
"""

import firebrowse
import json
import re
import download
import tarfile

class downloader():
    """
    Tools to help with downloading TCGA datasets.
    """
    @staticmethod
    def download(file_list):
        data = downloader.get_firehose_response()
        downloader.filter_objects(data)
        filenames = downloader.download_from_urls(data)
        downloader.untar_all(filenames)
        downloader.write_filenames(filenames,file_list)

    @staticmethod
    def get_firehose_response():
        resp = firebrowse.Archives().StandardData(cohort="brca", date='2015_06_01', data_type='CopyNumber,RPPA,Methylation', page="1", page_size="2000")
        return json.loads(resp)

    @staticmethod
    def include_obj(obj):
        if obj["sample_prep"] == "ffpe":
            return False
        elif obj["data_type"] == "Methylation" and ("platform" not in obj or obj["platform"] == "humanmethylation450"):
            return False
        else:
            return True

    @staticmethod
    def include_URL(url):
        if re.search("Level_3\.[0-9]{10}\.0\.0\.tar.gz$", url):
            return True
        else:
            return False

    @staticmethod
    def filter_objects(data):
        data["StandardData"] = [obj for obj in data["StandardData"] if downloader.include_obj(obj)]
        for i in range(len(data["StandardData"])):
            data["StandardData"][i]["urls"] = [url for url in data["StandardData"][i]["urls"] if downloader.include_URL(url)]

    @staticmethod
    def download_from_urls(data):
        filenames = []
        for obj in data["StandardData"]:
            fname = obj["urls"][0].split('/')[-1]
            download.download_file(obj["urls"][0], "./data/download/"+fname)
            filenames.append(fname)
        return filenames

    @staticmethod
    def untar(fname):
      if (fname.endswith("tar.gz")):
          tar = tarfile.open(fname)
          tar.extractall("./data/unzipped/")
          tar.close()

    @staticmethod
    def untar_all(filenames):
        for fname in filenames:
            downloader.untar("./data/download/"+fname)

    @staticmethod
    def write_filenames(filenames,file_list):
        with open(file_list, 'w') as f:
            f.write(json.dumps(filenames, indent=2, separators=(',', ': ')))


class preprocessor():
    """
    Tools to help with preprocessing and standardizing TCGA datasets.
    """
    @staticmethod
    def process(file_list):
        """
        Process all files listed in file_list from the downloads folder
        into a single data structure and then pickle to another file.

        First checks for the existence of the pickled file.
        """

        f = open(file_list, 'r')
        
        #gather the filenames for every type of preprocessing
        rpaa_list = []
        snp_list = []
        
        for file in f:
            if 'rpaa' in file.lower():
                rpaa_list.append(file)
                
            if 'snp' in file.lower():
                snp_list.append(file)
        
        f.close()
        
        print ("Processing...done")