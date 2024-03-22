#!/usr/bin/python3

import os, json, requests

from configs.settings import Settings

class ArxivDownload:
    
    @classmethod
    def download_pdf(url: str, filename: str) -> bool:
        response = requests.get(url)
    
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            
            return True
        else:
            return False
    
    @classmethod
    def make_download(self, pdf_link: str):
        print('TODO')
