from django.shortcuts import render
from careforyou.Model.models import Childcare


def get_the_childcare_info(id_list):
    list_childcares = []
    for id in id_list:
        childcares = Childcare.objects.filter(id=id)
        list_childcares.extend(childcares)
    return list_childcares


def get_save_list(request):
    if request.is_ajax():
        try:
            str_save = request.COOKIES['save_list']
        except KeyError:
            str_save = ''
        # split and remove empty str
        id_list = [id for id in str_save.split('%2C') if id != ""]
        # remove duplicates
        unique_id_list = list(set(id_list))
        count = len(unique_id_list)
        childcares = get_the_childcare_info(unique_id_list)
        context = {'count': count, 'childcares':childcares}
        return render(request, 'component/save_list.html', context)