# Generated by Django 4.1.5 on 2023-01-05 16:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tag', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('joined_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_kidan.account')),
            ],
        ),
        migrations.CreateModel(
            name='FollowingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='follower', to='api_kidan.account')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='following', to='api_kidan.account')),
            ],
        ),
    ]
