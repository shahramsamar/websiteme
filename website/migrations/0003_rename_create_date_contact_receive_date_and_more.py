# Generated by Django 4.2.8 on 2024-01-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_contact_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='create_date',
            new_name='receive_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='response_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
