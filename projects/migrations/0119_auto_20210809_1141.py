# Generated by Django 2.2.13 on 2021-08-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0118_auto_20210809_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcolumnpostfix',
            name='phases',
            field=models.ManyToManyField(related_name='report_columns', to='projects.CommonProjectPhase', verbose_name='phases'),
        ),
    ]
