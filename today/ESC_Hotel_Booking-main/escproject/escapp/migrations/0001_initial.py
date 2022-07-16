# Generated by Django 4.0.4 on 2022-05-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('Singapore', 'Singapore'), ('London', 'London'), ('Malaysia', 'Malaysia')], default='Singapore', max_length=250)),
                ('pax', models.IntegerField()),
            ],
        ),
    ]
