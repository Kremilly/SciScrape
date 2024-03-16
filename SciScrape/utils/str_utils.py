#!/usr/bin/python3

import unicodedata, json
import xml.etree.ElementTree as ET

class StrUtils:
    
    @classmethod
    def clean_string(self, string):
        return string.replace(
            '\n', ''
        ).strip()
    
    @classmethod
    def fix_unicode_name(self, name):
        return unicodedata.normalize(
            'NFD', name
        ).encode(
            'ascii', 'ignore'
        ).decode('utf-8')
        
    @classmethod
    def json_to_xml(self, data):
        data = json.loads(data)
        root = ET.Element('root')
        
        for key, value in data.items():
            if isinstance(value, dict):
                sub_element = ET.SubElement(root, key)
                sub_element.append(self.dict_to_xml(value))
                
            elif isinstance(value, list):
                for item in value:
                    sub_element = ET.SubElement(root, key)
                    sub_element.append(self.dict_to_xml(item))
            else:
                sub_element = ET.SubElement(root, key)
                sub_element.text = str(value)

        return root
