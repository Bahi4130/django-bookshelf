# Generated by Django 2.2.5 on 2019-09-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='borrowed_till',
            field=models.DateField(),
        ),
    ]