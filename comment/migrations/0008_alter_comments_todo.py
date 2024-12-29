# Generated by Django 5.0.6 on 2024-07-27 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0007_alter_comments_todo'),
        ('todo', '0005_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='todo.todo'),
        ),
    ]