#!/usr/bin/python3

import os
from datetime import date

from configs.settings import Settings

class FileUtils:
    
    @classmethod
    def make_folder(self, path: str, search: str = None, add_date: bool = True) -> str:
        folder = path
        
        if add_date == True:
            fmt_date = Settings.get('general.format_date', 'STRING')
            folder = os.path.join(folder, date.today().strftime(fmt_date))
        
        if search != None:
            folder = os.path.join(folder, search)
        
        os.makedirs(folder, exist_ok=True)        
        return folder
