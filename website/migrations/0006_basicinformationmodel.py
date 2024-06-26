# Generated by Django 4.2.8 on 2024-03-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
            ],
        ),
    ]
