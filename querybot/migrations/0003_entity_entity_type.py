# Generated by Django 2.2.1 on 2019-05-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('querybot', '0002_entityslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='entity_type',
            field=models.CharField(choices=[('manual', 'manual'), ('snips', 'snips')], default='', max_length=50),
        ),
    ]
