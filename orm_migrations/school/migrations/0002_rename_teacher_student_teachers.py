# Generated by Django 4.0.1 on 2022-06-10 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
