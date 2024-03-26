#!/usr/bin/python3

import os, json
from datetime import datetime

import xml.etree.ElementTree as ET

from configs.settings import Settings

from utils.file_utils import FileUtils

class ArxivHistory:
    
    @classmethod
    def get_current_time(self):
        current_time = datetime.now().time()
        return current_time.strftime("%H-%M-%S")

    @classmethod
    def export(self, json_data: json, xml_data: ET):
        if Settings.get('history.auto_save_history', 'BOOLEAN'):
            json_data_str = json.loads(json_data)
            cwd_path = Settings.get('history.output_folder', 'STRING')
            default_format = Settings.get('history.default_format', 'STRING')
            full_path = FileUtils.make_folder(cwd_path, json_data_str['search_term']) + '/' + self.get_current_time()
                    
            match (default_format):
                case 'xml': FileUtils.make_file(full_path + '.xml', xml_data, 'xml')
                case 'json': FileUtils.make_file(full_path + '.json', json_data, 'json')
                case '_': print('forat invalid')
