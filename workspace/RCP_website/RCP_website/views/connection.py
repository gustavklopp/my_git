from django.shortcuts import render

'''
views for connection page.
'''

def page(request):
    return render(request, 'en/public/connection.html')