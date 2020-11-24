# Generated by Django 3.0.4 on 2020-04-24 19:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
