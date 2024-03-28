#!/usr/bin/python3

import time
from datetime import datetime

from configs.settings import Settings

class TimeUtils:

    @classmethod
    def get_current_time(self):
        current_time = datetime.now().time()
        return current_time.strftime("%H-%M-%S")
    
    @classmethod
    def clean_date(sef, date):
        original_date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        date_time = Settings.get('general.format_date', 'STRING') + ' %H:%M:%S'
        return original_date.strftime(date_time)
    
    @classmethod
    def calculate_request_time(self, start_time: time, end_time: time) -> str:
        elapsed_time_seconds = end_time - start_time
        
        return str(
            round(elapsed_time_seconds * 1000)
        ) + ' ms'
