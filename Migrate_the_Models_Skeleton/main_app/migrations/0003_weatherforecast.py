# Generated by Django 4.2.4 on 2023-10-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('precipitation', models.FloatField()),
            ],
        ),
    ]
