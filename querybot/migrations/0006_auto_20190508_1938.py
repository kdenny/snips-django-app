# Generated by Django 2.2.1 on 2019-05-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querybot', '0005_utterance'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='metadata',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='entityrecord',
            name='metadata',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
