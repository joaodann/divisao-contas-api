# Generated by Django 3.1 on 2020-08-31 00:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisao', '0002_auto_20200830_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='members',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), blank=True, default=[], size=None),
            preserve_default=False,
        ),
    ]
