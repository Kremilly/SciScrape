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

    @classmethod
    def get(self, icon: str) -> str:
        if Settings.get('layout.show_icons', 'BOOLEAN'):
            return self[icon.upper()]
        
        return f"[{icon.capitalize().replace('_', ' ')}]"
