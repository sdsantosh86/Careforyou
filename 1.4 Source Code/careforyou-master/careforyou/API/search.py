from careforyou.Model.models import Childcare
from django.db.models import Q


def get_childcare_by_suburb_and_language(suburb, language):
    # function: find all childcare service based on the suburb
    # input: [string] suburb name, language name
    # output: [QuerySet] a list of Childcare object
    # If the selected language is "All", return result that meet the suburb criteria
    if language == "all":
        if suburb.isdigit():
            lst = Childcare.objects.filter(suburb_id__postcode__icontains=suburb)
        else:
            lst = Childcare.objects.filter(suburb_id__name__icontains=suburb)
    # If the selected language is not "All", return result that meet the suburb criteria and language criteria
    elif suburb == "":
        lst = Childcare.objects.filter(language_id__language=language)
    elif suburb.isdigit():
        lst = lst = Childcare.objects.filter(Q(suburb_id__postcode__icontains=suburb) & Q(language_id__language=language))
    else:
        lst = Childcare.objects.filter(Q(suburb_id__name__icontains=suburb) & Q(language_id__language=language))
    return lst


def get_childcare_by_postcode(postcode):
    # function: find all childcare service based on the postcode
    # input: [string] postcode
    # output: [QuerySet] a list of Childcare object
    lst = Childcare.objects.filter(postcode=postcode)
    return lst
