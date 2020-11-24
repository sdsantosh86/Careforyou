from django.http import HttpResponse
from django.utils.translation import gettext as _
import careforyou.API.language_tool as lt


def check_added(request):
    lt.change_language(request)
    if request.is_ajax():
        try:
            str_save = request.COOKIES['save_list']
            cid = request.GET['id']
        except KeyError:
            str_save = ''
        # split and remove empty str
        id_list = [id for id in str_save.split('%2C') if id != ""]
        # remove duplicates
        unique_id_list = list(set(id_list))
        for i in unique_id_list:
            if i == cid:
                return HttpResponse('<a href="#" class="d-none d-sm-inline-block btn btn-sm btn-success shadow-sm">'
                                    + '<i class="fas fa-check-circle fa-sm text-white-50"></i> '
                                    + _('Already in the SaveList')
                                    + '</a>')
        return HttpResponse('<a href="#" class="d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm" data-toggle="modal" data-target="#confirmModal">'
                            + '<i class="fas fa-download fa-sm text-white-50"></i> '
                            + _('Add to the SaveList')
                            + '</a>')
