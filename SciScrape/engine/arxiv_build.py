#!/usr/bin/python3

import json, time, requests

import xml.dom.minidom
import xml.etree.ElementTree as ET

from utils.str_utils import StrUtils
from utils.file_size import FileSize
from utils.pdf_utils import PdfUtils
from utils.time_utils import TimeUtils

from configs.settings import Settings
from configs.build_urls import BuildUrls

from engine.arxiv_get import ArxivGet
from engine.arxiv_bibtex import ArxivBibTex

class ArxivBuild:
    
    @classmethod
    def make_request(cls, search: str, max_results: int) -> object:
        headers = {}
        default_user_agent = Settings.get('general.default_user_agent', 'STRING')
        
        url = BuildUrls.api_search(
            search.replace(' ', '+'), max_results
        )
        
        if default_user_agent != '':
            headers['User-Agent'] = default_user_agent
        
        if Settings.get('general.disable_cache', 'BOOLEAN'):
            headers['Cache-Control'] = 'no-cache'
        
        return requests.get(url, headers=headers)
    
    @classmethod
    def get(cls, search: str, max_results: int) -> object:
        make_request = cls.make_request(search, max_results)
        arxiv_get = ArxivGet(make_request)
        
        return arxiv_get.get_json(
            search, max_results
        ), arxiv_get.get_xml(
            search, max_results
        )
