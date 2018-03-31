# Generated by Django 2.0.1 on 2018-03-02 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0008_poll_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('des', models.TextField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='lecturer1',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='lecturer2',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='lecturer3',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='votes',
        ),
        migrations.AddField(
            model_name='votes',
            name='vote',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='lecturer',
            name='votes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.Votes'),
        ),
        migrations.AddField(
            model_name='poll',
            name='lecturer',
            field=models.ManyToManyField(null=True, to='complaint.Lecturer'),
        ),
    ]