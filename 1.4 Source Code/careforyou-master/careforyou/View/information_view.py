from django.shortcuts import render
import careforyou.API.language_tool as lt


def get_view(request):
    lt.change_language(request)
    return render(request, 'information.html')