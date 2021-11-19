__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


# import Module

import os 
import shutil
import zipfile
import glob

# Dir Patch for lost file

dir_path = os.getcwd()
dir_cache = 'cache'
cache_folder = os.path.join(dir_path ,'cache')
zip_file = os.path.join(dir_path ,'data.zip')



# Opd 1

def clean_cache():
    if os.path.isdir(cache_folder):
        try:
            shutil.rmtree(cache_folder)
        except:
            print('Error while deleting directory')
    return os.makedirs(cache_folder)
        
# Opd 2

def cache_zip(zip_file, cache_folder):
    with zipfile.ZipFile(zip_file, 'r') as data:
        data.extractall(cache_folder)
    

# Opd 3

def cached_files():
    list = []
    for list in glob.glob('/files/cache/file?.txt'):
        return list

# Opd 4

def find_password(cache_folder):
   for file in cache_folder:
        with open(file) as check_file:
            lines = check_file.readlines()
            for line in lines:
                if 'password' in line: 
                     return line[line.find(' ') + 1:]  
                     
            


