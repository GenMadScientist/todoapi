# Generated by Django 5.0.6 on 2024-07-29 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_alter_todo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_list',
            field=models.CharField(max_length=30),
        ),
    ]
