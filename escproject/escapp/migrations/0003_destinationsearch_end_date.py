# Generated by Django 4.0.4 on 2022-05-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escapp', '0002_destinationsearch_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationsearch',
            name='end_date',
            field=models.DateField(default='2000-10-11'),
            preserve_default=False,
        ),
    ]