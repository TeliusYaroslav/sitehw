from django.shortcuts import render

# Create your views here.
def showautors(request):
    return render(request,"authors/authors.html")