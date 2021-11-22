__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


# import Module

import os 
import shutil
import zipfile


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
# voorbeeld 1 van opd 3 ad to do: werkt niet met de check??.

# def return_absolute_path():
#     abs_path_list = []
#     for file in os.listdir(cache_folder):
#         create_path = os.path.join(cache_folder, file)
#         abs_path_list.append(create_path)
#     return abs_path_list

def cached_files():
    abs_path_list = [os.path.join(cache_folder, file) for file in os.listdir(cache_folder)]
    return abs_path_list


    
#Opd 4

def find_password(file_paths):
    for x in file_paths:
        file = open(x, 'r')
        for line in file:
            if 'password' in line:
                password = line[line.find(" ") + 1 :-1]                  
                return password
  


