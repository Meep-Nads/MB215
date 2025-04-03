from django.shortcuts import render
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize ChatterBot
chatbot = ChatBot('EchoBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def homepage(request):
    return render(request, 'chatbot/homepage.html')

def chat_interface(request):
    user_message = request.GET.get('message', '')
    chatbot_response = chatbot.get_response(user_message)
    return JsonResponse({'response': str(chatbot_response)})