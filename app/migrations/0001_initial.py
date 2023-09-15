# Generated by Django 4.2.5 on 2023-09-15 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('providers_name', models.CharField(max_length=40)),
                ('pace', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shops_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
            ],
        ),
    ]
