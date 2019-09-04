# Generated by Django 2.2.5 on 2019-09-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('example_project_1', models.CharField(max_length=255)),
                ('example_project_2', models.CharField(max_length=255)),
            ],
        ),
    ]
