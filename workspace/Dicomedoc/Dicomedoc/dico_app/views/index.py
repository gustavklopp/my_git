from django.shortcuts import render
from dico_app.models import RcpTable
from django.http import JsonResponse #used for ajax

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

def dci_search(request):
    drugs_found = ''
    if request.method == 'GET':
        name = request.GET.get('search_text', '')
        import pdb; pdb.set_trace()
        print('name =' + name)
        drugs_found = RcpTable.objects.using('rcp_database').all().filter(nom_en_dci__startswith=name)
    return JsonResponse(drugs_found, safe=False)

def spec_search(request):
    drugs_found = ''
    if request.method == 'GET':
        name = request.GET.get('search_text', '')
        drugs_found = RcpTable.objects.using('rcp_database').all().filter(spec_name__startswith=name)
    return JsonResponse(drugs_found, safe=False)
