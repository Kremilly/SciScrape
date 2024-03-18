from enum import Enum

from configs.settings import Settings

class Icons(Enum):
    
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

    @classmethod
    def get(self, icon):
        if Settings.get('layout.show_icons', 'BOOLEAN'):
            return self[icon.upper()].value
        else:
            return f"[{icon.capitalize().replace('_', ' ')}]"
