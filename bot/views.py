from django.shortcuts import render
from django.http import HttpResponse
from .forms import BotForm
from .modules.pybot_weather import weather_command
from .modules.post_code import post_code_command
from datetime import date, datetime
import os


def index(request):
    msg = 'bot'
    context = {
        'title':msg,
        'today':f"今日は、{date.today().strftime('%Y/%m/%d, %A')}です。",
        'question':'your question?',
        'form':BotForm(),
        'input':'・郵便　〇〇市　〇〇区域」郵便No.が表示されます。<br>\
                ・「天気」白河市の天気が表示されます。<br>'
    }
    if request.method == 'POST':
        
        if '天気' in request.POST['questions']:
            context['question'] = weather_command()

        if '郵便' in request.POST['questions']:
            post_code = request.POST['questions']
            context['question'] = post_code_command(post_code)

    context['form'] = BotForm(request.POST)
    return render(request, os.path.join('bot','index.html'), context)
