from django.http import HttpResponse
from careforyou.utils import render_to_pdf
from django.utils.translation import gettext as _
from careforyou.Model.models import Childcare
import careforyou.API.language_tool as lt


def get_the_childcare_info(id_list):
    list_childcares = []
    for id in id_list:
        childcares = Childcare.objects.filter(id=id)
        list_childcares.extend(childcares)
    return list_childcares


def generate_pdf(request):
    lt.change_language(request)
    str_save = request.COOKIES['save_list']
    id_list = [id for id in str_save.split('%2C') if id != ""]
    unique_id_list = list(set(id_list))
    if len(unique_id_list) <= 0:
        return HttpResponse(_("ERROR: The savelist is empty."))
    childcare = get_the_childcare_info(unique_id_list)
    context = {
        "childcare":childcare
    }
    pdf = render_to_pdf('savelist.html', context)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="savelist.pdf"'
    return response