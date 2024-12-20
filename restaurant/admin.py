from django.contrib import admin
from .models import Gallery,DishCategory,Dishes,DishCategoryEmporter,DishesAEmporter,MySetting,Reviews,OppeningDay

admin.site.register(Gallery)
admin.site.register(DishCategory)
admin.site.register(Dishes)
admin.site.register(DishCategoryEmporter)
admin.site.register(DishesAEmporter)
admin.site.register(MySetting)
admin.site.register(Reviews)
admin.site.register(OppeningDay)

# Register your models here.
