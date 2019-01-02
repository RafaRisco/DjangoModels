# Generated by Django 2.1.4 on 2019-01-02 03:39

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_postmodel_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[blog.models.validate_author_email]),
        ),
    ]