# Generated by Django 4.0 on 2021-12-09 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
