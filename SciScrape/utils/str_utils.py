#!/usr/bin/python3

import unicodedata

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
