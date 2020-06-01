# Generated by Django 3.0.6 on 2020-05-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiSearchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.CharField(max_length=10)),
                ('hotel_destination_code', models.CharField(max_length=3)),
                ('hotel_name', models.CharField(max_length=100)),
                ('hotel_street', models.CharField(max_length=100)),
                ('hotel_city', models.CharField(max_length=100)),
                ('hotel_state', models.CharField(max_length=100)),
                ('hotel_country', models.CharField(max_length=100)),
                ('hotel_zip', models.CharField(max_length=100)),
                ('hotel_curr', models.CharField(max_length=10)),
                ('hotel_amt', models.FloatField()),
                ('hotel_inserted', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
