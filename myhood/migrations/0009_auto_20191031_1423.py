# Generated by Django 2.2.6 on 2019-10-31 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0008_auto_20191031_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesses',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myhood.Neighbourhood'),
        ),
    ]