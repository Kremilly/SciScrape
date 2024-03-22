#!/usr/bin/python3

import os, json, requests
from datetime import date

from configs.settings import Settings

class ArxivDownload:
    
    @classmethod
    def open_folder(self, folder_path: str):
        try:
            os.startfile(folder_path)
        except Exception as e:
            return e
    
    @classmethod
    def make_folder(self, search: str) -> str:
        today = date.today()
        cwd_path = Settings.get('downloads.downloads_folder', 'STRING')
        
        main_folder = cwd_path + '/' + today.strftime("%Y-%m-%d")
        os.makedirs(main_folder, exist_ok=True)
        
        sub_folder = os.path.join(main_folder, search)
        os.makedirs(sub_folder, exist_ok=True)
        
        return sub_folder
    
    @classmethod
    def download_pdf(self, url: str, filename: str, path: str) -> bool:
        response = requests.get(url)
        
        full_path = os.path.join(path, filename)
    
        if response.status_code == 200:
            with open(full_path, 'wb') as f:
                f.write(response.content)
            
            return True
        else:
            return False
    
    @classmethod
    def make_download(self, json_data: json):
        if Settings.get('downloads.auto_download_papers', 'BOOLEAN'):
            json_data = json.loads(json_data)
            path = self.make_folder(json_data['search_term'])

            if 'articles' in json_data:
                articles = json_data['articles']
                
                for article in articles:
                    self.download_pdf(
                        article['links']['pdf']['url'],
                        article['links']['pdf']['name'],
                        path
                    )
                    
            if Settings.get('downloads.auto_open_folder', 'BOOLEAN'):
                self.open_folder(path)
