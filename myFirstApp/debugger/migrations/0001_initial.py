# Generated by Django 3.0.5 on 2020-05-19 16:09

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
                ('status', models.CharField(choices=[('1', 'reported'), ('2', 'checked'), ('3', 'solved')], default='reported', max_length=80)),
                ('heading', models.CharField(max_length=100)),
                ('discription', models.CharField(default=' ', max_length=200)),
                ('media_upload', models.CharField(default=' ', max_length=200)),
                ('reported_on', models.DateTimeField(auto_now=True, null=True, verbose_name='date published')),
                ('last_updated_on', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Last Updated On')),
                ('tag', models.CharField(choices=[('1', 'design'), ('2', 'dev'), ('3', 'UI'), ('4', 'Ux')], default='dev', max_length=20)),
                ('assigned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_by', to='debugger.User')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to='debugger.User')),
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
