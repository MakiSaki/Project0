from django.shortcuts import render

# Create your views here.
def mywebpage(request):
    return render(request, 'mywebpage.html', {})