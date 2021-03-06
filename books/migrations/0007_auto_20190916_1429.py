# Generated by Django 2.2.5 on 2019-09-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20190916_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_by_who',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowed_till',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
