# Generated by Django 3.2.6 on 2022-03-04 18:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='blogContent',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
