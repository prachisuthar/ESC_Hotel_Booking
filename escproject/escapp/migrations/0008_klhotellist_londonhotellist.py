# Generated by Django 3.2.7 on 2022-07-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escapp', '0007_alter_singaporehotellist_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='KLHotelList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_hotel', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='kl')),
                ('hotel_room', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LondonHotelList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_hotel', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='london')),
                ('hotel_room', models.PositiveIntegerField()),
            ],
        ),
    ]