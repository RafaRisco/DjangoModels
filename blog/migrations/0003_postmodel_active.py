# Generated by Django 2.1.4 on 2018-12-31 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181231_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
