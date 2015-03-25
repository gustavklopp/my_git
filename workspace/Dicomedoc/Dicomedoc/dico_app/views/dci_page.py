from django.shortcuts import render
from dico_app.models import RcpTable

# view for dci_page.
def page(request, rcp_id):
    drug_rcp = RcpTable.objects.using('rcp_database').get(rcp_id=rcp_id)
    import pdb; pdb.set_trace()
    return render(request, 'dci_page.html', {'drug_rcp':drug_rcp})

