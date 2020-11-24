from django.shortcuts import render
import careforyou.API.search as search_tool
import careforyou.API.language_tool as lt


def get_view(request):
    lt.change_language(request)
    if request.method == 'GET':
        para = dict(request.GET)
    else:
        para = dict(request.POST)

    # extract query content from parameter dict....
    suburb = para['q'][0]
    try:
        language = para['language'][0]
    except KeyError:
        # if the input not include language option, by default set it as all
        language = 'all'

    # by default, the query will be suburbs
    # need to be improved ( add validation )
    list_childcare = search_tool.get_childcare_by_suburb_and_language(suburb, language)
    context = {'results': list_childcare, 'service_count': len(list_childcare), 'suburb': suburb, 'language': language}

    if len(list_childcare) <=0:
        return render(request, '404.html', context)
    return render(request, 'result.html', context)