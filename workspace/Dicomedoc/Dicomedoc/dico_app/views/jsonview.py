from django.http import JsonResponse #used for ajax
import json #used for ajax
from dico_app.models import RcpTable

def dci_search(request):
    drugs_found = ''
    if request.method == 'GET':
        name = request.GET.get('search_text', '')
        try:
            drugs_found = RcpTable.objects.using('rcp_database').values("rcp_id", "spec_name").filter(nom_en_dci__startswith=name)
        except:
            pass
    # print(drugs_found)
    drugs_found_json = json.dumps(list(drugs_found))
    return JsonResponse(drugs_found_json, safe=False)

def spec_search(request):
    drugs_found = ''
    if request.method == 'GET':
        name = request.GET.get('search_text', '')
        try:
            drugs_found = RcpTable.objects.using('rcp_database').values("rcp_id", "spec_name").filter(spec_name__startswith=name)
        except:
            pass
    drugs_found_json = json.dumps(list(drugs_found))
    return JsonResponse(drugs_found_json, safe=False)

