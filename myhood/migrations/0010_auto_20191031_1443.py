# Generated by Django 2.2.6 on 2019-10-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0009_auto_20191031_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesses',
            name='user',
        ),
        migrations.AddField(
            model_name='businesses',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/business/'),
        ),
    ]
