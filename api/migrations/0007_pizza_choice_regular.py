# Generated by Django 3.0.8 on 2021-05-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_pizza_choice_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza_choice',
            name='regular',
            field=models.BooleanField(default=True, verbose_name='Regular'),
        ),
    ]
