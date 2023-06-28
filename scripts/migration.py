#!/usr/bin/env python3
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()
# Read the config file
config.read('config.ini')
# Get the value of the variable from the config file
STORAGE_SY = config.get('Settings', 'storage_system')

if STORAGE_SY == 'LOCAL':
    from local_storage import Storage
    storage = Storage('file_storage')

elif STORAGE_SY == 'AWS':
    pass

# List of files to migrate
# get files from file_storage
files = storage.get_files()
for file in files:
    # read file and store to postgres databese
    



