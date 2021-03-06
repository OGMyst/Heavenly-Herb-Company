# Generated by Django 3.1.5 on 2021-01-09 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20201129_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address1', models.CharField(max_length=254)),
                ('street_address2', models.CharField(max_length=254)),
                ('town_or_city', models.CharField(max_length=254)),
                ('county', models.CharField(max_length=254)),
                ('country', models.CharField(max_length=254)),
                ('postcode', models.CharField(max_length=254)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]
