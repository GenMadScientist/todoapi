# Generated by Django 5.0.6 on 2024-07-15 17:34

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_remove_comment_successful'),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('user', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('todo', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='todo.todo')),
            ],
        ),
    ]
