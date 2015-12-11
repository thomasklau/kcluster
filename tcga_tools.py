"""
Helpful tools for downloading and processing TCGA data from The Broad Institute.
"""

import firebrowse
import json
import re
import download
import tarfile
import os
import numpy as np

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
      if (fname.endswith('tar.gz')):
          tar = tarfile.open(fname)
          tar.extractall('./data/unzipped/')
          tar.close()

    @staticmethod
    def untar_all(filenames):
        for fname in filenames:
            downloader.untar('./data/download/'+fname)

    @staticmethod
    def getDataFolders():
        '''
        Return the names of all the folders in the unzipped data folder in
        the form of an array
        '''
        
        folders = []
        for name in os.listdir('./data/unzipped'):
                folders.append(name)
            
        return folders
    
    @staticmethod
    def rename_all_data():
        folders = downloader.getDataFolders()
        
        subdirectory = []
        for folder in folders:
            for name in os.listdir('./data/unzipped/' + folder):
                if ('Level_3' in name or 'rppa' in name):
                    os.rename('./data/unzipped/' + folder + '/' + name, './data/unzipped/' + folder + '/data.txt')

    @staticmethod
    def write_filenames(filenames,file_list):
        with open(file_list, 'w') as f:
            f.write(json.dumps(filenames, indent=2, separators=(',', ': ')))

class preprocessor():
    """
    Tools to help with preprocessing and standardizing TCGA datasets.
    """
    
    @staticmethod
    def processRPPA(rppaFolders, theta):
        for folder in rppaFolders:
            if 'annotatewithgene' in folder.lower():
                array = np.genfromtxt('./data/unzipped/' + folder + '/data.txt', dtype=None, delimiter = '\t')
                array = np.transpose(array)
                totalarray = []
                
                for i in range(0,len(array)):
                    if i == 0:
                        continue
                    
                    patient_id = array[i][0]
                    if patient_id not in theta:
                        theta[patient_id] = []
                    
                    theta[patient_id].append(array[i][1:])
            else:
                array = np.genfromtxt('./data/unzipped/' + folder + '/data.txt', dtype=None, delimiter = '\t')
                array = np.transpose(array)
                
                for i in range(0,len(array)):
                    if i == 0:
                        continue
                    
                    patient_id = array[i][0]
                    if patient_id not in theta:
                        theta[patient_id] = []
                    
                    theta[patient_id].append(array[i][2:])
                    
    @staticmethod
    def process():
        """
        Process all files listed in file_list from the downloads folder
        into a single data structure and then pickle to another file.

        First checks for the existence of the pickled file.
        """
        
        theta = {} #dict to store all of the patient vectors
        
        folders = downloader.getDataFolders()

        # gather the folders for every type of preprocessing
        # Note: The data in each folder is named 'data.txt'
        rppa_list = []
        snp_list = []
        cnv_list = []
        
        for folder in folders:
            
            if 'rppa' in folder.lower():
                rppa_list.append(folder)

            if 'snp' in folder.lower():
                snp_list.append(folder)
                
            if 'cnv' in folder.lower():
                cnv_list.append(folder)
                
        preprocessor.processRPPA(rppa_list, theta)
        
        print theta
        print ("Processing...done")