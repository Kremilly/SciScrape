#!/usr/bin/python3

import pyfiglet

from configs.env import Env

from rich.console import Console

from layout.icons import Icons

from engine.arxiv_build import ArxivBuild

console = Console()

class ArxivUI:

    @classmethod
    def run(self, search, max_results):
        console.print(f"[red]{pyfiglet.figlet_format(Env.APP_NAME)}[/red]")
        console.print("-" * 60) 

        console.print(
            ArxivBuild.get_json(
                search, max_results
            )
        )
