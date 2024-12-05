# Generated by Django 5.1.3 on 2024-12-05 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_dishes_dish_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='dishes',
            name='dish_menu_type',
        ),
        migrations.AddField(
            model_name='dishcategory',
            name='category_menu_type',
            field=models.ManyToManyField(to='restaurant.categorychoices'),
        ),
        migrations.AddField(
            model_name='dishes',
            name='category_menu_type',
            field=models.ManyToManyField(to='restaurant.categorychoices'),
        ),
    ]
