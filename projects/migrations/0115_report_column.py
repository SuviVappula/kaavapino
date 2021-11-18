# Generated by Django 2.2.13 on 2021-06-24 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0114_document_template_common_project_phase'),
    ]

    def migrate_report_columns(apps, schema_editor):
        ReportAttribute = apps.get_model('projects', 'ReportAttribute')
        ReportColumn = apps.get_model('projects', 'ReportColumn')

        for report_attr in ReportAttribute.objects.all():
            column = ReportColumn.objects.create(report=report_attr.report)
            column.attributes.set([report_attr.attribute])

    operations = [
        migrations.CreateModel(
            name='ReportColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField(default=0, verbose_name='index')),
                ('attributes', models.ManyToManyField(related_name='report_columns', to='projects.Attribute', verbose_name='attributes')),
                ('condition', models.ManyToManyField(related_name='report_column_conditions', to='projects.Attribute', verbose_name='condition')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='projects.Report', verbose_name='report')),
            ],
            options={
                'verbose_name': 'report column',
                'verbose_name_plural': 'report columns',
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='ReportColumnPostfix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatting', models.CharField(max_length=255, verbose_name='formatting')),
                ('phases', models.ManyToManyField(related_name='report_columns', to='projects.CommonProjectPhase', verbose_name='')),
                ('report_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postfixes', to='projects.ReportColumn', verbose_name='report column')),
            ],
            options={
                'verbose_name': 'report column postfix',
                'verbose_name_plural': 'report column postfixes',
                'ordering': ('id',),
            },
        ),
        migrations.RunPython(migrate_report_columns, migrations.RunPython.noop),
        migrations.DeleteModel(
            name='ReportAttribute',
        ),
    ]