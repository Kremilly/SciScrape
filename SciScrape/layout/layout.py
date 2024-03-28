#!/usr/bin/python3

import pyfiglet

from rich.console import Console

from layout.icons import Icons

from configs.env import Env
from configs.settings import Settings

console = Console()

class Layout:
    
    @classmethod
    def header(self):
        if Settings.get('layout.show_header', 'BOOLEAN'):
            app_name = pyfiglet.figlet_format(Env.APP_NAME)
            
            console.print(f"[red]{app_name}[/red]")
            console.print("-" * 60)
