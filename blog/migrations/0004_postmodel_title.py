# Generated by Django 2.1.4 on 2018-12-31 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postmodel_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New Title', max_length=250),
        ),
    ]
