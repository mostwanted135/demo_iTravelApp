# Generated by Django 3.0.6 on 2020-05-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_pnrconfirmedlist_pnr_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnrconfirmedlist',
            name='pnr_pic',
            field=models.CharField(max_length=50),
        ),
    ]
