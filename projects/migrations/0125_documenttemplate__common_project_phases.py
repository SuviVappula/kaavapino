# Generated by Django 2.2.13 on 2021-08-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0124_reportfilter_reportfilterattributechoice'),
    ]

    def set_common_project_phases(apps, schema_editor):
        DocumentTemplate = apps.get_model('projects', 'DocumentTemplate')

        for template in DocumentTemplate.objects.all():
            template.common_project_phases.set([
                template.common_project_phase
            ])

    operations = [
        migrations.AddField(
            model_name='documenttemplate',
            name='common_project_phases',
            field=models.ManyToManyField(related_name='document_templates', to='projects.CommonProjectPhase', verbose_name='project phases'),
        ),
        migrations.RunPython(set_common_project_phases, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='documenttemplate',
            name='common_project_phase',
        ),
    ]
