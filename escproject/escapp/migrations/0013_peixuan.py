# Generated by Django 3.2.7 on 2022-07-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escapp', '0012_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeiXuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
    ]
