# Generated by Django 2.1.5 on 2019-02-12 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190212_1532'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='gettagcode',
            name='final_TagCode_66bd77_idx',
        ),
    ]
