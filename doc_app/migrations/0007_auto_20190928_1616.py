# Generated by Django 2.1.7 on 2019-09-28 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc_app', '0006_auto_20190928_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='first_name',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name',
            new_name='start_time',
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set(),
        ),
    ]
