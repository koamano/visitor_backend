# Generated by Django 3.0 on 2019-12-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_auto_20191216_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
