# Generated by Django 2.0.5 on 2018-07-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20180723_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='enckey',
            field=models.CharField(default=' ', max_length=2048),
        ),
        migrations.AddField(
            model_name='file',
            name='sha256',
            field=models.CharField(default=' ', max_length=256),
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(default=' '),
        ),
    ]
