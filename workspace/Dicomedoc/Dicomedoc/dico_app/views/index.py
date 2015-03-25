from django.shortcuts import render
from dico_app.models import RcpTable

# view for index page.
def page(request):
    drugs_found = ''
    if 'search_text' in request.GET:
        name = request.GET.get('search_text', '')
    if 'search_type' in request.GET:
        search_type = request.GET.get('search_type', '')
        if search_type == 'dci':
            drugs_found = RcpTable.objects.using('rcp_database').all().filter(nom_en_dci__startswith=name)
        else:
            drugs_found = RcpTable.objects.using('rcp_database').all().filter(spec_name__startswith=name)
    return render(request, 'index.html', {'drugs_found':drugs_found})
