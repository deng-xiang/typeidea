# Generated by Django 3.1.1 on 2020-09-19 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
