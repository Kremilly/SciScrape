#!/usr/bin/python3

import json

from rich import print_json
from rich.console import Console

from layout.icons import Icons
from layout.layout import Layout

from configs.settings import Settings

from utils.time_utils import TimeUtils

from engine.arxiv_build import ArxivBuild
from engine.arxiv_history import ArxivHistory
from engine.arxiv_download import ArxivDownload

from exceptions.settings_exception import SettingsException

console = Console()

class ArxivUI:
    
    @classmethod
    def get_visual_mode(self, json_data: json):
        json_data = json.loads(json_data)
        
        console.print(f"{Icons.get('timer')} Request time: {json_data['calculate_request_time']} | "
                      f"{Icons.get('stats')} Status code {json_data['status_code']} | "
                      f"{Icons.get('total')} Total of articles: {json_data['total']}")
        
        console.print('-' * 60)
        
        if 'articles' in json_data:
            articles = json_data['articles']
            
            for article in articles:
                console.print(f"{Icons.get('title')} [blue bold]{article['title']}[/blue bold]")
                console.print('-' * 60)
                
                console.print(f"> {Icons.get('doc')} Basic")
                
                console.print(" - [blue bold]ID[/blue bold]:", article['id'])
                console.print(" - [blue bold]Title[/blue bold]:", article['title'])
                console.print(" - [blue bold]Summary[/blue bold]:", article['summary'])
                console.print(" - [blue bold]E-print[/blue bold]:", article['eprint'])
                
                console.print(f"> {Icons.get('user')} Authors")
                for author in article['authors']:
                    console.print(f" - [blue bold][link={author['url']}]{author['name']}[/link][/blue bold]")
                    
                console.print(f"> {Icons.get('tag')}  Categories")
                for category in article['categories']:
                    console.print(f" - [blue bold][link={category['url']}]{category['name']}[/link][/blue bold]")
                
                console.print(f"> {Icons.get('link')} Links")
                if 'doi' in article['links']:
                    console.print(f" - [blue bold][link={article['links']['doi']}]DOI[/link][/blue bold]")
                    
                console.print(f" - [blue bold][link={article['links']['page']}]Page[/link][/blue bold]")
                console.print(f" - [blue bold][link={article['links']['pdf']['url']}]Document[/link][/blue bold] (Size: {article['links']['pdf']['size']} | Pages: {article['links']['pdf']['pages']})")
                console.print(f" - [blue bold][link={article['links']['src']['url']}]Source[/link][/blue bold] (Size: {article['links']['src']['size']})")
                
                console.print(f"> {Icons.get('date')} Dates")
                console.print(f" - Published: {TimeUtils.clean_date(article['date']['published'])}")
                console.print(f" - Updated: {TimeUtils.clean_date(article['date']['updated'])}")
                
                console.print("-" * 60)

    @classmethod
    def run(self, search: str, max_results: int):
        mode = Settings.get('layout.default_mode', 'STRING')
        json_data, xml_data = ArxivBuild.get(search, max_results)
        
        Layout.header()
        
        match(mode):
            case 'json':
                print_json(json_data)
                
            case 'xml':
                print(xml_data)
                
            case 'visual':
                self.get_visual_mode(json_data)
                
            case _:
                wrong_property_position = Settings.get_wrong_property_position('default_mode')
                raise SettingsException(f"Invalid layout default mode. It should be either JSON, XML or Visual." 
                                        f"{wrong_property_position}.")
        
        ArxivDownload.download(json_data)
        ArxivHistory.save(json_data, xml_data)
