# Generated by Django 3.0.8 on 2021-05-02 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210502_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza_choice',
            name='phone',
        ),
    ]