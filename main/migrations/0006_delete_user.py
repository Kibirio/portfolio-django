# Generated by Django 3.1.7 on 2021-03-23 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_user_visit_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
