# Generated by Django 2.2.5 on 2019-09-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20190916_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrowed_by_who',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
