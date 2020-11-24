"""careforyou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from careforyou.View import password_view, index_view, \
    result_view,detail_view, \
    about_view, \
    information_view
from careforyou.API import ajax_get_savelist, ajax_get_language, download_list, ajax_check_added

urlpatterns = [
    path('',password_view.get_view),
    path('home', index_view.get_view),
    path('details',detail_view.get_view),
    path('search', result_view.get_view),
    path('about/',about_view.get_view),
    path('get_language', ajax_get_language.get_language_list),
    path('get_savelist', ajax_get_savelist.get_save_list),
    path('generate_pdf', download_list.generate_pdf),
    path('information/', information_view.get_view),
    path('check_added',ajax_check_added.check_added),
]