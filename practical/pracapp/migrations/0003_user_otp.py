# Generated by Django 3.2.16 on 2022-12-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pracapp', '0002_auto_20221215_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(default=0),
        ),
    ]