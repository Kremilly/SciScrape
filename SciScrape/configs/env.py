#!/usr/bin/python3

class Env:
    
    LICENSE = 'MIT'
    VERSION = '0.0.5'
    AUTHOR = 'Kremilly'
    APP_NAME = 'SciScrape'
    CONFIGS_FILE = './sciscrape.yml'
    HOMEPAGE = 'https://github.com/Kremilly/SciScrape'
    
    BASE_URL = 'http://arxiv.org/'
    SEARCH_BASE = f'{BASE_URL}search'
    API_BASE = f"{BASE_URL.replace('//', '//export.')}api/"
    
    RANDOM_STR = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
