# Generated by Django 2.2.5 on 2019-09-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20190916_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_till',
            field=models.DateField(null=True),
        ),
    ]
