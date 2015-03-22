from django.shortcuts import render
from dico_app.models import RcpTable

# view for index page.
def page(request):
    if 'search_text' in request.GET:
        name = request.GET.get('search_text', '')
    drug_found = RcpTable.objects.get()
    return render(request, 'dci_page.html', {'name':name})

