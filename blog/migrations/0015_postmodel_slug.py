# Generated by Django 2.1.4 on 2019-01-02 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190101_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
