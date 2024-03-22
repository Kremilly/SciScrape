#!/usr/bin/python3

from configs.settings import Env
from configs.settings import Settings

class BuildUrls:
    
    @classmethod
    def api_search(self, search_term: str, max_results: int) -> str:
        search_term = search_term.replace(' ', '+')
        endpoint = f'{Env.API_BASE}query?search_query=all:{search_term}&start=0&max_results={max_results}'
        
        if Settings.get('general.force_https', 'BOOLEAN'):
            return endpoint.replace('http', 'https')
        
        return endpoint
    
    @classmethod
    def author_page_link(self, author_name: str) -> str:
        author = author_name.replace(' ', '+')
        return f'{Env.SEARCH_BASE}?searchtype=author&query={author}&abstracts=show&order=-announced_date_first&size=50'

    @classmethod
    def category_search_link(self, category: str) -> str:
        return f'{Env.SEARCH_BASE}?query={category}&searchtype=all&abstracts=show&order=-announced_date_first&size=50'

    @classmethod
    def source_link(self, abs_link: str) -> str:
        return abs_link.replace('pdf', 'src')
