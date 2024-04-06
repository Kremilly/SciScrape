#!/usr/bin/python3

import unicodedata, json
import xml.etree.ElementTree as ET

class StrUtils:
    
    @classmethod
    def clean_string(cls, string):
        return string.replace(
            '\n', ''
        ).strip()
    
    @classmethod
    def fix_unicode_name(cls, name):
        return unicodedata.normalize(
            'NFD', name
        ).encode(
            'ascii', 'ignore'
        ).decode('utf-8')
        
    @classmethod
    def json_to_xml(cls, data: json) -> ET:
        root = ET.Element('root')
        
        for key, value in data.items():
            sub_element = ET.SubElement(root, key)
            
            if isinstance(value, dict):
                sub_element.append(cls.json_to_xml(value))
                
            elif isinstance(value, list):
                for item in value:
                    sub_element.append(cls.json_to_xml(item))
            else:
                sub_element.text = str(value)

        return root
