# Generated by Django 2.2.5 on 2019-09-16 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190914_1148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
