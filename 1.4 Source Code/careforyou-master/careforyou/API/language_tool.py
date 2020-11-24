from django.utils.translation import activate


def change_language(request):
    lang = request.COOKIES.get('careforyou_language')
    if lang is not None:
        activate(lang)