# Generated by Django 4.2.5 on 2023-11-19 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_helprequest_contain_of_help'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helprequest',
            name='status_of_help',
        ),
    ]
