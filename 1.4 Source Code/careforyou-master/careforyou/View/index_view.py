from django.shortcuts import render
from careforyou.Model.models import Language
import careforyou.API.news as newstool
import careforyou.API.language_tool as lt


def get_view(request):
    
   
           
    lt.change_language(request)
    language_list = get_all_distinct_languages()
    try:
        news = newstool.get_news()['articles']
    except KeyError:
        news = None
    context = {'language_list': language_list,'news' : news}
    if request.method == 'POST':
       password=request.POST.get('password')
       if password != 'careforyou':
        return render(request, 'error.html', context)
    return render(request, 'landing.html', context)


def get_all_distinct_languages():
    languages = Language.objects.values('language').distinct()
    return languages

