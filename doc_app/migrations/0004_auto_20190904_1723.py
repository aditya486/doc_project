# Generated by Django 2.1.7 on 2019-09-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_app', '0003_auto_20190326_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.CharField(max_length=100),
        ),
    ]