# Generated by Django 5.1.3 on 2024-12-05 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_remove_dishes_dish_menu_type'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dishcategory',
            table='catégorie de plat du menu En salle',
        ),
        migrations.AlterModelTable(
            name='dishes',
            table='plat du menu En salle',
        ),
    ]
