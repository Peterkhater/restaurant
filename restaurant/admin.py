from django.contrib import admin
from .models import Gallery,DishCategory,Dishes,DishCategoryEmporter,DishesAEmporter

admin.site.register(Gallery)
admin.site.register(DishCategory)
admin.site.register(Dishes)
admin.site.register(DishCategoryEmporter)
admin.site.register(DishesAEmporter)

# Register your models here.
