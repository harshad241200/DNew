# Generated by Django 4.0.4 on 2022-05-05 12:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 12, 42, 31, 861362, tzinfo=utc)),
        ),
    ]
