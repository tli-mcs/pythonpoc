import os
import time

class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_size(self):
        return os.path.getsize(self.file_path)

    def get_creation_time(self):
        return time.ctime(os.path.getctime(self.file_path))

    def get_last_modified_time(self):
        return time.ctime(os.path.getmtime(self.file_path))

if __name__ == "__main__":
    file_info = FileInfo('C:\Ting\Azure Blueprint\service-blueprint-template.pdf')
    print('Size:', file_info.get_size())
    print('Creation Time:', file_info.get_creation_time())
    print('Last Modified Time:', file_info.get_last_modified_time())