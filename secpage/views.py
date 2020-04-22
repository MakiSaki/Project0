from django.shortcuts import render

# Create your views here.
def secpage(request):
    return render(request, 'secpage.html', {})