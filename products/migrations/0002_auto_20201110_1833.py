# Generated by Django 3.1.3 on 2020-11-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='product',
            name='directions',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
    ]
