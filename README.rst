==================
Django ChatBot AI
==================

A Django wrapper with webhook for  `ChatbotAI<https://pypi.org/project/chatbotAI/>`


`Example code<https://github.com/ahmadfaizalbh/WebBot>`



Installation
============
::

  pip install django-chatbot
  
 

Usage
======
in settings.py add the following::

   INSTALLED_APPS = [
    ...
    'django.chatbot',
    ...
  ]
 
  CHATBOT_TEMPLATE = <ChatBotAI template file path>
  START_MESSAGE = "Welcome to ChatBotAI"


in urls.py add the following::

  from django.chatbot.views import web_hook
  
  
  urlpatterns = [
    ...
    path("webhook/", web_hook, name="webhook"),
    ...
 ]


Web Hook API (should authenticate before API request)
============
::

  URL: /webhook/
  Method: POST
  Data: {
          last_message_id: 5,
          message: "what is dosa"
        }
  Response: {
        "status": "Success",
        "messages": [
             {
               "id": 6, "text": "what is dosa", 
               "created": "2020-03-22 19:42:59",
               "by": "user"
              }, {
                "id": 7, 
                "text": "A dosa is a cooked flat thin layered rice batter, originating from South India, made from a fermented batter....", 
                "created": "2020-03-22 19:42:59", 
                "by": "bot"
              }
        ]
  }
  
