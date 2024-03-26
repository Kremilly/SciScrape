#!/usr/bin/python3

import os, json, requests

from configs.settings import Settings

from utils.file_utils import FileUtils

class ArxivDownload:
    
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
    def download(self, json_data: json) -> None:
        if Settings.get('downloads.auto_download_papers', 'BOOLEAN'):
            json_data = json.loads(json_data)
            cwd_path = Settings.get('downloads.downloads_folder', 'STRING')
            path = FileUtils.make_folder(cwd_path, json_data['search_term'])

            if 'articles' in json_data:
                articles = json_data['articles']
                
                for article in articles:
                    url, name = article['links']['pdf']['url'], article['links']['pdf']['name']
                    self.download_pdf(url, name, path)
                    
            if Settings.get('downloads.auto_open_folder', 'BOOLEAN'):
                os.startfile(path)
