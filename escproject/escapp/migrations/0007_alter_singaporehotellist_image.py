# Generated by Django 3.2.7 on 2022-07-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escapp', '0006_auto_20220711_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singaporehotellist',
            name='image',
            field=models.ImageField(upload_to='singapore'),
        ),
    ]