#!/usr/bin/python3

import json, pyfiglet, asyncio

from rich import print_json
from rich.console import Console

from layout.icons import Icons

from configs.env import Env
from configs.settings import Settings

from engine.arxiv_build import ArxivBuild
from engine.arxiv_download import ArxivDownload

console = Console()

class ArxivUI:
    
    @classmethod
    def get_visual_mode(self, json_data: json):
        print('hello')

    @classmethod
    def run(self, search, max_results):
        json_data = asyncio.run(ArxivBuild.get_json(search, max_results))
        
        console.print(f"[red]{pyfiglet.figlet_format(Env.APP_NAME)}[/red]")
        console.print("-" * 60)
        
        print_json(json_data)
        ArxivDownload.make_download(json_data)
