# Generated by Django 4.2.11 on 2024-12-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_recipe_ingredient_4_recipe_ingredient_5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_req',
            field=models.CharField(default='in pot', max_length=200),
        ),
    ]
