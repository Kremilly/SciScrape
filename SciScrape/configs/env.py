#!/usr/bin/python3

class Env:
    
    VERSION = '0.0.3'
    APP_NAME = 'SciScrape'
    CONFIGS_FILE = './sciscrape.yml'
    HOMEPAGE = 'https://github.com/Kremilly/SciScrape'
    
    BASE_URL = 'http://arxiv.org/'
    SEARCH_BASE = f'{BASE_URL}search'
    API_BASE = f"{BASE_URL.replace('//', '//export.')}api/"
