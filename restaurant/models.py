from django.db import models

class Gallery(models.Model):
    images = models.ImageField(upload_to='photos', null=False, blank=False)
    text = models.CharField(blank=True, null=True, max_length=200)

   
class DishCategory(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True)
    note = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.category or "Unnamed Category"
    class Meta:
        verbose_name = 'catégorie de plat du menu En salle'



class Dishes(models.Model):
    dish_name = models.CharField(max_length=255, null=True, blank=True)
    dish_price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_description = models.TextField(null=True, blank=True)
    dish_images = models.ImageField(upload_to='photos', null=True, blank=True)
    dish_category = models.ForeignKey(
        DishCategory, 
        on_delete=models.CASCADE, 
        related_name='dishes', 
        null=True, 
        blank=True
    )
    def __str__(self):
        return f"{self.dish_name}"
    
    class Meta:
        verbose_name = 'plat du menu En salle'
        



class DishCategoryEmporter(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True)
    note = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.category or "Unnamed Category"
    class Meta:
        verbose_name = 'catégorie de plat du menu a(Emporter)'


class DishesAEmporter(models.Model):
    dish_name = models.CharField(max_length=255, null=True, blank=True)
    dish_price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_description = models.TextField(null=True, blank=True)
    dish_images = models.ImageField(upload_to='photos', null=True, blank=True)
    dish_category = models.ForeignKey(
        DishCategoryEmporter, 
        on_delete=models.CASCADE, 
        related_name='dishes', 
        null=True, 
        blank=True
    )
    def __str__(self):
        return f"{self.dish_name}"
    
    class Meta:
        verbose_name = 'plat du menu menu a (Emporter)'

class MySetting(models.Model):
   phone = models.CharField( max_length=40,  blank=True, null=True)
   email = models.EmailField(max_length=254, null=True, blank=True)
   instagramLink = models.TextField(blank=True, null=True)
   facebookLink = models.TextField(blank=True, null=True)
   website_url = models.URLField(max_length=200, blank=True, null=True)
   address = models.CharField(max_length=255, blank=True, null=True)
   business_name = models.CharField(max_length=100, blank=True, null=True)
   logo = models.ImageField(upload_to='photos', blank=True, null=True)
   linkedinLink = models.URLField(max_length=200, blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   description = models.TextField(blank=True, null=True)
   owner_name = models.CharField(max_length=100, blank=True, null=True)
   owner_img =  models.ImageField(upload_to='photos', blank=True, null=True)