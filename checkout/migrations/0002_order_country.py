# Generated by Django 3.1.3 on 2020-11-22 15:53

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(default='UK', max_length=2),
        ),
    ]
