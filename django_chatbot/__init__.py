from .chatbot import chat


VERSION = (0, 0, 1)
__version__ = '.'.join(map(str, VERSION))

default_app_config = 'django.chatbot.apps.DjangoChatBotConfig'
