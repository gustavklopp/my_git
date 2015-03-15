from django.shortcuts import render

# view for index page.
def page(request):
    return render(request, 'index.html')
