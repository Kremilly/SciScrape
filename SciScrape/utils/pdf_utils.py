#!/usr/bin/python3

import os, requests

from PyPDF2 import PdfReader
from tempfile import NamedTemporaryFile

class PdfUtils:

    @classmethod
    def download_pdf(cls, url: str, filename: str, path: str) -> bool:
        response = requests.get(url)
        full_path = os.path.join(path, filename)
    
        if response.status_code == 200:
            with open(full_path, 'wb') as f:
                f.write(response.content)
            
            return True
        
        return False

    @classmethod
    def get_pdf_page_count(cls, url: str) -> int|None:
        response = requests.get(url)
        
        if response.status_code == 200:
            with NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(response.content)
                temp_file.seek(0)
                pdf_file = PdfReader(temp_file.name)
            
            return len(pdf_file.pages)
            
        return None
