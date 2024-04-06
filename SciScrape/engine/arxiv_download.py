#!/usr/bin/python3

import os, json

from configs.settings import Settings

from utils.pdf_utils import PdfUtils
from utils.file_utils import FileUtils

class ArxivDownload:
    
    @classmethod
    def download(cls, json_data: json) -> None:
        if Settings.get('downloads.auto_download_papers', 'BOOLEAN'):
            json_data = json.loads(json_data)
            cwd_path = Settings.get('downloads.downloads_folder', 'STRING')
            path = FileUtils.make_folder(cwd_path, json_data['search_term'])

            if 'articles' in json_data:
                articles = json_data['articles']
                
                for article in articles:
                    url, name = article['links']['pdf']['url'], article['links']['pdf']['name']
                    PdfUtils.download_pdf(url, name, path)
                    
            if Settings.get('downloads.auto_open_folder', 'BOOLEAN'):
                os.startfile(path)
