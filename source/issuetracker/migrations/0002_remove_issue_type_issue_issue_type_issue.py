# Generated by Django 4.1.2 on 2022-10-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='type_issue',
        ),
        migrations.AddField(
            model_name='issue',
            name='type_issue',
            field=models.ManyToManyField(blank=True, related_name='issues', to='issuetracker.typeissue', verbose_name='Тип'),
        ),
    ]
