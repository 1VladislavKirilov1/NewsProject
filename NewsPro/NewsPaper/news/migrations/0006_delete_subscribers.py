# Generated by Django 4.2.1 on 2023-06-07 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_subscribers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscribers',
        ),
    ]
