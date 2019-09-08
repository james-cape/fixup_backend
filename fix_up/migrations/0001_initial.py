# Generated by Django 2.2.5 on 2019-09-08 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('example_project_1', models.CharField(max_length=255)),
                ('example_project_2', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=255)),
                ('user_before_picture', models.CharField(max_length=255)),
                ('user_after_picture', models.CharField(max_length=255, null=True)),
                ('contractors', models.ManyToManyField(blank=True, related_name='contractor_list', to='fix_up.Contractor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fix_up.User')),
            ],
        ),
        migrations.CreateModel(
            name='ContractorProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor_choice', models.IntegerField(default=0)),
                ('user_choice', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('contractor_before_picture', models.CharField(default=None, max_length=1000, null=True)),
                ('contractor_after_picture', models.CharField(default=None, max_length=1000, null=True)),
                ('user_rating', models.IntegerField(default=None, null=True)),
                ('contractor_rating', models.IntegerField(default=None, null=True)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fix_up.Contractor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fix_up.Project')),
            ],
        ),
        migrations.AddField(
            model_name='contractor',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='project_list', to='fix_up.Project'),
        ),
    ]
