#!/usr/bin/python3

import time, requests

from PyPDF2 import PdfReader
from tempfile import NamedTemporaryFile

class ArxivUtils:
    
    @classmethod
    def calculate_request_time(self, start_time: time, end_time: time) -> str:
        elapsed_time_seconds = end_time - start_time
        
        return str(
            round(elapsed_time_seconds * 1000)
        ) + ' ms'
        
    @classmethod
    def get_pdf_page_count(self, url: str):
        response = requests.get(url)
        
        if response.status_code == 200:
            with NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(response.content)
                temp_file.seek(0)
                pdf_file = PdfReader(temp_file.name)
            
            return len(pdf_file.pages)
        else:
            return None
