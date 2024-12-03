from django.shortcuts import render
from .models import Gallery

def main(request):
    gallery = Gallery.objects.all()
    return render(request,'index.html',{'gallery':gallery})