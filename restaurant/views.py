from django.shortcuts import render
from .models import Gallery,DishCategory,Dishes,DishCategoryEmporter,DishesAEmporter,MySetting,Reviews,OppeningDay

def main(request):
    gallery = Gallery.objects.all()
    setting = MySetting.objects.last()
    reviews = Reviews.objects.all()
    oppeningDay = OppeningDay.objects.all()
    return render(request,'index.html',{'gallery':gallery,'setting':setting,'reviews':reviews,'openingDay':oppeningDay})

def menu(request):
    categories = DishCategory.objects.prefetch_related('dishes').all()
    setting = MySetting.objects.last()
    return render(request, 'menu.html', {'cat': categories,'setting':setting})


def menuEmporter(request):
    categories = DishCategoryEmporter.objects.prefetch_related('dishes').all()
    setting = MySetting.objects.last()
    return render(request, 'menu_emporte.html', {'cat': categories,'setting':setting})
