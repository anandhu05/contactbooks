# Generated by Django 4.0.2 on 2022-06-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('phone_number', models.CharField(default=None, max_length=20)),
                ('email', models.EmailField(default=None, max_length=100)),
            ],
        ),
    ]
