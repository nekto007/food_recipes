# Generated by Django 4.2.5 on 2023-09-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_remove_recipe_category_recipe_category'),
        ('users', '0006_alter_subscription_options_alter_vote_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='allergies', to='recipes.category', verbose_name='Аллергии'),
        ),
    ]
