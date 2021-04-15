# Generated by Django 2.2.13 on 2021-04-13 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0103_projectcardsection_projectcardsectionattribute'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentLinkSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('index', models.PositiveIntegerField(default=0, verbose_name='index')),
            ],
            options={
                'verbose_name': 'document link section',
                'verbose_name_plural': 'document link sections',
                'ordering': ('index',),
            },
        ),
        migrations.CreateModel(
            name='DocumentLinkFieldSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_custom_name_attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custom_name_in_document_fieldsets', to='projects.Attribute', verbose_name='document custom name attribute')),
                ('document_link_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link_in_document_fieldsets', to='projects.Attribute', verbose_name='document link attribute')),
                ('document_name_attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name_in_document_fieldsets', to='projects.Attribute', verbose_name='document name attribute')),
                ('fieldset_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_fieldsets', to='projects.Attribute', verbose_name='fieldset attribute')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.DocumentLinkSection')),
            ],
            options={
                'verbose_name': 'document link fieldset',
                'verbose_name_plural': 'document link fieldsets',
            },
        ),
    ]