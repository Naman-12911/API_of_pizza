# Generated by Django 3.2 on 2021-05-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pizza_choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('phone', models.IntegerField()),
                ('choose_pizza', models.CharField(max_length=100)),
                ('pizza_size', models.CharField(max_length=100)),
                ('toppings', models.CharField(max_length=150)),
            ],
        ),
    ]
