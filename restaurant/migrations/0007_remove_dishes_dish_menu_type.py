# Generated by Django 5.1.3 on 2024-12-05 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_remove_dishcategory_category_menu_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishes',
            name='dish_menu_type',
        ),
    ]