
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chatbot import chat
from .models import Conversation
from django.conf import settings


@csrf_exempt
@login_required
def web_hook(request):
    sender_id = request.user.username
    last_message_id = None
    if sender_id not in chat.conversation:
        chat.start_new_session(sender_id)
        chat.conversation[sender_id].append_bot(getattr(settings, "START_MESSAGE",
                                                        "Welcome to ChatBotAI"))
    if request.method == "POST":
        message = request.POST.get("message")
        last_message_id = request.POST.get("last_message_id")
        if message:
            chat.attr[sender_id] = {'match': None,
                                    'pmatch': None,
                                    '_quote': False,
                                    'substitute': True}
            chat.conversation[sender_id].append_user(message)
            message = message.rstrip(".! \n\t")
            result = chat.respond(message, session_id=sender_id)
            chat.conversation[sender_id].append_bot(result)
            del chat.attr[sender_id]
    msgs = Conversation.objects.filter(sender__messengerSenderID=sender_id)
    if last_message_id:
        msgs = msgs.filter(id__gt=last_message_id)
    count = msgs.count()
    msgs = msgs.order_by("id")
    if count > 50:
        msgs = msgs[50:]
    return JsonResponse({
        "status": "Success",
        "messages": [{"id": msg.id,
                      "text": msg.message,
                      "created": msg.created.strftime('%Y-%m-%d %H:%M:%S'),
                      "by": "bot" if msg.bot else "user"
                      } for msg in msgs]
        })
