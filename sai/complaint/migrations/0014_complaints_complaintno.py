# Generated by Django 2.0.1 on 2018-03-03 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0013_auto_20180303_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='complaintno',
            field=models.IntegerField(default=0),
        ),
    ]
