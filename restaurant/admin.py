from django.contrib import admin
from .models import Gallery,DishCategory,Dishes,DishCategoryEmporter,DishesAEmporter,MySetting

admin.site.register(Gallery)
admin.site.register(DishCategory)
admin.site.register(Dishes)
admin.site.register(DishCategoryEmporter)
admin.site.register(DishesAEmporter)
admin.site.register(MySetting)

# Register your models here.
