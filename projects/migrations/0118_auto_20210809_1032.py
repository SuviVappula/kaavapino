# Generated by Django 2.2.13 on 2021-08-09 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0117_reportcolumn_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='show_name',
        ),
        migrations.RemoveField(
            model_name='report',
            name='show_phase',
        ),
        migrations.RemoveField(
            model_name='report',
            name='show_subtype',
        ),
        migrations.RemoveField(
            model_name='report',
            name='show_user',
        ),
        migrations.AddField(
            model_name='report',
            name='previewable',
            field=models.BooleanField(default=False, verbose_name='report can be previewed'),
        ),
    ]
