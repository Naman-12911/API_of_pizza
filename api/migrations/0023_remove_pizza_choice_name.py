# Generated by Django 3.0.5 on 2021-06-20 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_pizza_choice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza_choice',
            name='name',
        ),
    ]