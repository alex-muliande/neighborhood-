# Generated by Django 2.2.6 on 2019-10-31 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0006_auto_20191031_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesses',
            name='neighbourhood',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myhood.Neighbourhood'),
        ),
    ]
