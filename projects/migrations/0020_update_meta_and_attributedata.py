# Generated by Django 2.0.1 on 2018-10-16 11:05

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_add_project_phase_log'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('name',), 'verbose_name': 'project', 'verbose_name_plural': 'projects'},
        ),
        migrations.AlterField(
            model_name='project',
            name='attribute_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True, verbose_name='attribute data'),
        ),
    ]
