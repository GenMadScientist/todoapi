# Generated by Django 5.0.6 on 2024-07-15 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
