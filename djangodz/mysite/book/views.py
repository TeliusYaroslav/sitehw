from django.shortcuts import render

# Create your views here.
def showbook(request):
    return render(request,"book/book.html")