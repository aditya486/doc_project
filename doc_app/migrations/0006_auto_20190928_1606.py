# Generated by Django 2.1.7 on 2019-09-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_app', '0005_hurricane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.DateTimeField(),
        ),
    ]