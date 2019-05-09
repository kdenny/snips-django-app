# Generated by Django 2.2.1 on 2019-05-07 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('querybot', '0004_delete_utterance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utterance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utterances', to='querybot.Intent')),
            ],
        ),
    ]