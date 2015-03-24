from django.shortcuts import render
from dico_app.models import RcpTable

# view for dci_page.
def page(request):
    if 'search_text' in request.GET:
        name = request.GET.get('search_text', '')
    if 'search_type' in request.GET:
        search_type = request.GET.get('search_type', '')
    if search_type == 'dci':
        drug_found = RcpTable.objects.using('rcp_database').get(nom_en_dci=name)
    else:
        drug_found = RcpTable.objects.using('rcp_database').get(spec_name=name)
    return render(request, 'dci_page.html', {'name':name, 'drug_found':drug_found})

