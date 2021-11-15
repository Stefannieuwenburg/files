__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'


import os 
import shutil
import zipfile


dir_path = os.getcwd()
dir_cashe = 'cache'
cache_folder = dir_path + '\\cache'
zip_file = dir_path + '\\data.zip'



# Opd 1

def clean_cache():
    dir_path = os.getcwd()
    cache_folder = f'{dir_path}/files/cache';
    if os.path.isdir(cache_folder):
        try:
            shutil.rmtree(cache_folder)
        except:
            print('Error while deleting directory')
    return os.mkdir(cache_folder)
        
# Opd 2

def cache_zip(zip_file, cache_dir):
    clean_cache()
    with zipfile.ZipFile(zip_file, 'r') as data:
        data.extractall(cache_folder)
    return(cache_zip(zip_file, cache_dir))

# Opd 3

def cached_files():
    cache_path_list = [os.path.join(dir_cashe, file)
    for file
        in os.listdir(cache_folder)]
    return cache_path_list


# Opd 4

def find_password(cached_folder):
   for file in cached_folder:
        txt_file = open(file, "r")
        for line in txt_file:
            if "password" in line:
                password = line[line.find(" ")+1:-1]
                txt_file.close
        return password        





