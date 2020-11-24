from django.shortcuts import render
from careforyou.Model.models import Language


def get_language_list(request):
    if request.is_ajax():
        # get value in search box
        suburb = request.GET.get('suburb')
        # if user input nothing, return all exist language in dropdown list
        if suburb == "":
            language_list = Language.objects.values('language').distinct()
        # if user type suburb, return language supported by the childcare that meet suburb criteria
        elif suburb.isdigit() == True:
            language_list = Language.objects.filter(childcare__suburb_id__postcode__icontains=suburb).values('language').distinct()
        else:
            language_list = Language.objects.filter(childcare__suburb_id__name__icontains=suburb).values('language').distinct()      
        context = {'language_list': language_list}
        return render(request, 'component/language_list.html', context)
