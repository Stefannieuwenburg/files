__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# import Modules

import os
import glob
import zipfile

# path to

path = os.getcwd()
files = glob.glob('cache/*')

# Opd 1

def clean_cache():
    if os.path.exists('cache'):
        files = glob.glob('cache/*')
        for file in files:
            os.removedirs(file)
    else:
        os.makedirs('cache')

# Opd 2

def cache_zip(zip_file_path, cache_dir_path):
    my_zip_file = zipfile(zip_file_path, 'r')
    my_zip_file.extractall(cache_dir_path)


# Opd 3

def cached_files():
    return glob.glob('cache/*')

# Opd 4

def find_password(list):
    files = list
    check_file = []
    for file in files:
        if "password" in open(file, 'r').read():
            check_file.append(file)
    lines = open(check_file[0], 'r').readlines()
    for line in lines:
        line.replace('\n', '')
        position = line.find('password')
        if position != -1:
            return line.split(' ')[1]
        
        
print(find_password("password")) # Oeps geen password ??
