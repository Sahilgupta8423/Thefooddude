# Generated by Django 3.1.3 on 2021-01-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tfd', '0009_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='help',
            name='textarea',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
