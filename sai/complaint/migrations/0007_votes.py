# Generated by Django 2.0.1 on 2018-03-02 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0006_auto_20180219_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.Choice')),
            ],
        ),
    ]
