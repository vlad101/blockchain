# Generated by Django 2.0 on 2017-12-20 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171220_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Block'),
        ),
    ]