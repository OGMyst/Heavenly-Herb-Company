# Generated by Django 3.1.5 on 2021-01-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address_number',
            field=models.CharField(default='', editable=False, max_length=32),
            preserve_default=False,
        ),
    ]
