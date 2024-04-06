#!/usr/bin/python3

import os, json
from datetime import date

from configs.settings import Settings

class FileUtils:

    @classmethod
    def make_file(cls, path: str, content, fmt: str):
        with open(path, 'w') as f:
            if fmt == 'json':
                if isinstance(content, str):
                    f.write(content)
                else:
                    json.dump(content, f, indent=Settings.get('general.json_indent_size', 'INT'))
            else:
                f.write(content)
    
    @classmethod
    def make_folder(cls, path: str, search: str = None, add_date: bool = True) -> str:
        folder = path
        
        if add_date:
            fmt_date = Settings.get('general.format_date', 'STRING')
            folder = os.path.join(folder, date.today().strftime(fmt_date))
        
        if search is not None:
            folder = os.path.join(folder, search)
        
        os.makedirs(folder, exist_ok=True)        
        return folder
