# Generated by Django 5.0.4 on 2024-05-06 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nilai', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nilai',
            old_name='student_id',
            new_name='npm_id',
        ),
    ]
