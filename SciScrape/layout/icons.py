#!/usr/bin/python3

from configs.settings import Settings

class Icons:
    
    USER = "👤"
    DOC = "📄"
    SOURCE = "📝"
    DOWNLOAD = "💾"
    DATE = "📅"
    TAG = "🏷️"
    LINK = "🔗"
    SUMMARY = "📑"
    SEARCH = "🔍"
    TITLE = "📚"
    WARNING = "⚠️"
    ERROR = "❌"
    STATS = "📊"
    TIMER = "⏰"
    TOTAL = "🔢"
    BIBTEX = "📑"
    VERSION = "🔖"
    HOME = "🏠"
    LICENSE = "📜"

    @classmethod
    def get(cls, icon: str) -> str:
        if Settings.get('layout.show_icons', 'BOOLEAN'):
            return getattr(cls, icon.upper())
        
        return f"[{icon.capitalize().replace('_', ' ')}]"
