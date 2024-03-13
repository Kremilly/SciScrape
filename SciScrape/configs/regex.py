#!/usr/bin/python3

import re
from enum import Enum

class Regex(Enum):
    
    MAX_RESULTS = r'^[1-9]\d*$'
    
    @classmethod
    def is_valid(self, value, type):
        return re.match(
            self[type].value, value
        ) is not None
