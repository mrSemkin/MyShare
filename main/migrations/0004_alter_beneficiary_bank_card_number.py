# Generated by Django 4.2.5 on 2023-11-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_helprequest_status_of_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='bank_card_number',
            field=models.CharField(max_length=16, null=True),
        ),
    ]