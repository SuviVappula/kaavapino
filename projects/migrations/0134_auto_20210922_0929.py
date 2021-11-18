# Generated by Django 2.2.13 on 2021-09-22 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0133_reportcolumn_postfix_only'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportcolumnpostfix',
            name='phases',
        ),
        migrations.AddField(
            model_name='reportcolumnpostfix',
            name='subtypes',
            field=models.ManyToManyField(related_name='report_columns', to='projects.ProjectSubtype', verbose_name='subtypes'),
        ),
    ]