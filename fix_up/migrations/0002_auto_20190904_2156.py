# Generated by Django 2.2.5 on 2019-09-04 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fix_up', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contractors',
            old_name='specialty',
            new_name='category',
        ),
    ]
