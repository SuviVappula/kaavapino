# Generated by Django 2.1.2 on 2018-11-02 11:20

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_attribute_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhaseAttributeMatrixCell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField()),
                ('column', models.IntegerField()),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectPhaseSectionAttribute')),
            ],
        ),
        migrations.CreateModel(
            name='PhaseAttributeMatrixStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('row_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectPhaseSection', verbose_name='phase section')),
            ],
        ),
        migrations.AddField(
            model_name='phaseattributematrixcell',
            name='structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.PhaseAttributeMatrixStructure'),
        ),
    ]
