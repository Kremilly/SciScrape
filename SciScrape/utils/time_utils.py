#!/usr/bin/python3

import time
from datetime import datetime

class TimeUtils:

    @classmethod
    def get_current_time(self):
        current_time = datetime.now().time()
        return current_time.strftime("%H-%M-%S")
    
    @classmethod
    def calculate_request_time(self, start_time: time, end_time: time) -> str:
        elapsed_time_seconds = end_time - start_time
        
        return str(
            round(elapsed_time_seconds * 1000)
        ) + ' ms'
