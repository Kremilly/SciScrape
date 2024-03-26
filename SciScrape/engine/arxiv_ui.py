#!/usr/bin/python3

import json

from rich import print_json
from rich.console import Console

from layout.icons import Icons
from layout.layout import Layout

from configs.settings import Settings

from engine.arxiv_build import ArxivBuild
from engine.arxiv_history import ArxivHistory
from engine.arxiv_download import ArxivDownload

console = Console()

class ArxivUI:
    
    @classmethod
    def get_visual_mode(self, json_data: json):
        print('TODO')

    @classmethod
    def run(self, search: str, max_results: int):
        json_data, xml_data = ArxivBuild.get(search, max_results)
        
        Layout.header()
        
        print_json(json_data)
        
        ArxivDownload.download(json_data)
        ArxivHistory.save(json_data, xml_data)
