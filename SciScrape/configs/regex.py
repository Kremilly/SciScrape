#!/usr/bin/python3

import re
from enum import Enum

class Regex(Enum):
    
    MAX_RESULTS = r'^[1-9]\d*$'
    
    @classmethod
    def is_valid(self, value, regex):
        return re.match(
            self[regex].value, value
        ) is not None
