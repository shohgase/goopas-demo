# Generated by Django 3.2.5 on 2021-07-29 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_playertaskstate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlayerTaskState',
        ),
    ]
