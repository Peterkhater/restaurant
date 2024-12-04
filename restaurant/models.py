from django.db import models

class Gallery(models.Model):
    images = models.ImageField(upload_to='photos', null=False, blank=False)
    text = models.CharField(blank=True, null=True, max_length=200)

   
class DishCategory(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True)
    note = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.category or "Unnamed Category"



class Dishes(models.Model):
    MENU_CHOICES = [
        ('emporter', 'Menu à Emporter'),
        ('ensalle', 'Menu en Salle'),
    ]
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
    dish_menu_type = models.CharField(
        max_length=20, 
        choices=MENU_CHOICES, 
        default='ensalle'
    )
    def __str__(self):
        return f"{self.dish_name}"