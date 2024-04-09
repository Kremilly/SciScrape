#!/usr/bin/python3

from engine.arxiv_ui import ArxivUI

from configs.flags import Flags
from configs.settings import Settings

default_max_results = Settings.get('results.default_max_results', 'INT')

flags = Flags.parser("Usage: python sciscrape -s 'astronomy' -m 5", [
    {'short': 's', 'long': 'search', 'help': 'Search of articles', 'required': True},
    {'short': 'm', 'long': 'max-results', 'help': 'Maximium of results', 'required': False, 'default': default_max_results},
])

if __name__ == '__main__':
    ArxivUI.run(flags.search, flags.max_results)
