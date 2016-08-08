# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 20:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('academic_year', models.IntegerField()),
                ('semester', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'FAL Class',
                'verbose_name_plural': 'FAL Classes',
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'LMS',
                'verbose_name_plural': 'LMS',
            },
        ),
        migrations.CreateModel(
            name='LMS_Web_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_service_name', models.CharField(max_length=128)),
                ('web_service_method', models.CharField(max_length=128)),
                ('web_service_url', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'LMS Web Service',
                'verbose_name_plural': 'LMS Web Services',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('url', models.CharField(max_length=128)),
                ('lms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foraliving.LMS')),
            ],
        ),
        migrations.CreateModel(
            name='User_Add_Ons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foraliving.LMS')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foraliving.School')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Add-ons',
                'verbose_name_plural': 'User Add-ons',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=128)),
                ('my_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Commenter', to='foraliving.User_Add_Ons')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='foraliving.Video')),
            ],
            options={
                'verbose_name': 'Video Comment',
                'verbose_name_plural': 'Video Comments',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='foraliving.User_Add_Ons'),
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviewee', to='foraliving.User_Add_Ons'),
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviewer', to='foraliving.User_Add_Ons'),
        ),
        migrations.AddField(
            model_name='class',
            name='lms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foraliving.LMS'),
        ),
        migrations.AddField(
            model_name='class',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foraliving.School'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Teacher', to='foraliving.User_Add_Ons'),
        ),
        migrations.AddField(
            model_name='answer',
            name='my_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Provided By+', to='foraliving.User_Add_Ons'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foraliving.Question'),
        ),
    ]
