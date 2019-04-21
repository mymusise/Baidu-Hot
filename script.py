import os
import json
from datetime import datetime


class Viwer():
    ROOT = './data'
    CATEGORY = ['entertainment', 'life', 'sports', 'today', 'sevent_day']

    def __init__(self, data_folder=''):
        if data_folder:
            self.ROOT = data_folder

    def get_files(self, start_time, end_time, category):
        files = []
        for name in category:
            path = os.path.join(self.ROOT, category)
            start_path = os.path.join(path, start_time.strftime("%Y/%m-%d"))
            end_path = os.path.join(path, end_time.strftime("%Y/%m-%d"))
            names = os.popen(f"find {path} |grep json").read().split('\n')
            names = list(filter(lambda x: start_path < x < end_path, names))
            names = sorted(names)
            files += names
        return files

    def view(self, start_time, end_time, category=[], top=None):
        start_time = datetime.strptime(start_time, "%Y-%m-%d")
        end_time = datetime.strptime(end_time, "%Y-%m-%d")
        if category == []:
            category = self.CATEGORY

        files = self.get_files(start_time, end_time, category)
        print(files)
        for f in files:
            _, _, category, year, day = f.split('/')
            time = f"{year}-{day.split('.')[0]}"
            data = json.load(open(f))
            data = sorted(data, key=lambda x: x['search_index'], reverse=True)
            for item in data:
                print(time, item['keyword'], item['search_index'])


