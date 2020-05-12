# Generated by Django 3.0.5 on 2020-05-12 13:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('image', models.ImageField(upload_to='image')),
                ('contact', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('wiki', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='debugger.User')),
                ('team_member', models.ManyToManyField(related_name='team_member', to='debugger.User')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('reported', '1'), ('checked', '2'), ('solved', '3')], default='reported', max_length=80)),
                ('heading', models.CharField(max_length=100)),
                ('discription', models.CharField(default=' ', max_length=200)),
                ('media_upload', models.CharField(default=' ', max_length=200)),
                ('reported_on', models.DateTimeField(auto_now=True, null=True, verbose_name='date published')),
                ('last_updated_on', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Last Updated On')),
                ('tag', models.CharField(choices=[('design', '1'), ('dev', '2'), ('UI', '3'), ('Ux', '4')], default='dev', max_length=20)),
                ('assigned_to', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='debugger.User')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debugger.Project')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debugger.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commented_by', to='debugger.User')),
                ('issue_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debugger.Issue')),
                ('mention', models.ManyToManyField(related_name='mentions', to='debugger.User')),
            ],
        ),
    ]
