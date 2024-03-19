#!/usr/bin/python3

import argparse

from engine.arxiv_ui import ArxivUI
from configs.settings import Settings

default_max_results = Settings.get('results.default_max_results', 'INT')

parser = argparse.ArgumentParser(description="Usage: python sciscrape -s 'astronomy' -max 5")

parser.add_argument("-s", "--search", help="Search of articles", required=True)
parser.add_argument("-max", "--max-results", help="Maximum of results", default=default_max_results)

args = parser.parse_args()

if __name__ == '__main__':
    ArxivUI.run(args.search, args.max_results)
