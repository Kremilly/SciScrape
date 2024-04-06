#!/usr/bin/python3

import re

class Regex:
    
    STRING_TYPE = r"^.*$"
    INT_TYPE = r"^[0-9]\d*$"
    FLOAT_TYPE = r"^\d+\.\d+$"
    BOOLEAN_TYPE = r"^(?i)(true|false)$"

    @classmethod
    def is_valid(cls, value, regex):
        return re.match(
            cls[regex.upper()], value
        ) is not None
