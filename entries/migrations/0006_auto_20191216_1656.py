# Generated by Django 3.0 on 2019-12-17 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0005_auto_20191215_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='signout_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
