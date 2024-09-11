# Generated by Django 2.2.5 on 2021-06-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CropRecommendationApp', '0002_auto_20210607_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='crop_recommed',
            fields=[
                ('cr_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Crop Recommend ID')),
                ('cr_farmername', models.CharField(max_length=100, verbose_name='Farmer Name')),
                ('cr_nitrogen', models.PositiveIntegerField(max_length=10, verbose_name='Soil Nitrogen')),
                ('cr_phosphorous', models.PositiveIntegerField(max_length=10, verbose_name='Soil Phosphorous')),
                ('cr_potassium', models.PositiveIntegerField(max_length=10, verbose_name='Soil Potassium')),
                ('cr_ph', models.FloatField(max_length=10, verbose_name='Soil ph')),
                ('cr_temperature', models.FloatField(max_length=10, verbose_name='Soil Temperature')),
                ('cr_humidity', models.FloatField(max_length=10, verbose_name='Relative Humidity')),
                ('cr_rainfall', models.FloatField(max_length=10, verbose_name='Rainfall')),
                ('cr_crop', models.CharField(max_length=10, verbose_name='Recommended Crop')),
            ],
        ),
    ]
