#!/usr/bin/python3

import json

import xml.etree.ElementTree as ET

from configs.settings import Settings
from utils.file_utils import FileUtils
from utils.time_utils import TimeUtils

from exceptions.arxiv_exception import ArxivException

class ArxivHistory:

    @classmethod
    def save(cls, json_data: json, xml_data: ET):
        if Settings.get('history.auto_save_history', 'BOOLEAN'):
            json_data_str = json.loads(json_data)
            cwd_path = Settings.get('history.output_folder', 'STRING')
            default_format = Settings.get('history.default_format', 'STRING')
            full_path = FileUtils.make_folder(cwd_path, json_data_str['search_term']) + '/' + TimeUtils.get_current_time()

            match default_format:
                case 'xml':
                    FileUtils.make_file(full_path + '.xml', xml_data, 'xml')
                case 'json':
                    FileUtils.make_file(full_path + '.json', json_data, 'json')
                case _:
                    wrong_property_position = Settings.get_wrong_property_position('default_format')
                    raise ArxivException(f"Invalid history file format. It should be either XML or JSON. {wrong_property_position}.")
