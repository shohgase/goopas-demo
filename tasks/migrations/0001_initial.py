# Generated by Django 3.2.5 on 2021-07-15 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_results', '0010_remove_duplicate_indices'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerTaskState',
            fields=[
                ('taskresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_celery_results.taskresult')),
            ],
            bases=('django_celery_results.taskresult',),
        ),
    ]
