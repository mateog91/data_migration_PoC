import os

class Storage:
    def __init__(self, storage_path):
        self.storage_path = '../file_storage/landing_zone/'

    def get_files(self):
        """
        Get the list of files to migrate from file_storage folder that are csv files
        """
        files = os.listdir(self.storage_path)
        files = [file for file in files if file.endswith('.csv')]
        return files


    def get(self, key):
        with open(self.storage_path, 'r') as f:
            data = json.load(f)
            return data[key]

    def set(self, key, value):
        with open(self.storage_path, 'r') as f:
            data = json.load(f)
            data[key] = value
        with open(self.storage_path, 'w') as f:
            json.dump(data, f)