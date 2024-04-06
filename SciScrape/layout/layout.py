#!/usr/bin/python3

import pyfiglet

from rich.console import Console

from layout.icons import Icons

from configs.env import Env
from configs.settings import Settings

console = Console()

class Layout:

    @classmethod
    def header(cls):
        if Settings.get('layout.show_header', 'BOOLEAN'):
            app_license = Env.LICENSE
            app_homepage = Env.HOMEPAGE
            app_author_user = f"@{Env.AUTHOR}"
            app_name = pyfiglet.figlet_format(Env.APP_NAME)
            app_author_url = Env.HOMEPAGE.replace(f"/{Env.APP_NAME}", '')

            console.print(f"[red]{app_name}[/red]")

            console.print(f"{Icons.get('version')} {Env.VERSION} | "
                          f"{Icons.get('license')} {app_license} | "
                          f"{Icons.get('user')} [blue bold link={app_author_url}]{app_author_user}[/blue bold link] | "
                          f"{Icons.get('home')} [blue bold link={app_homepage}]Homepage[/blue bold link]")

            console.print("-" * 60)
