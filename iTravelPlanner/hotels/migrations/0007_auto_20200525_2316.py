# Generated by Django 3.0.6 on 2020-05-26 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_auto_20200525_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apireturnlist',
            name='hotel_pic',
            field=models.CharField(max_length=50),
        ),
    ]
