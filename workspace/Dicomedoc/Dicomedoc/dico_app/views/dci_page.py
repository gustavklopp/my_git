from django.shortcuts import render

# view for index page.
def page(request):
    if 'search_text' in request.GET:
        name = request.GET.get('search_text', '')
    return render(request, 'dci_page.html', {'name':name})

