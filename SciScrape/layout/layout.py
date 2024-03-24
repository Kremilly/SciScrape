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
            
            if Settings.get('layout.show_colors', 'BOOLEAN'):
                console.print(f"[red]{app_name}[/red]")
            else:
                print(app_name)
            
            console.print("-" * 60)
