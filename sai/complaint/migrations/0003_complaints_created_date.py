# Generated by Django 2.0.1 on 2018-02-12 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0002_auto_20180212_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]