# Generated by Django 2.2.13 on 2020-08-25 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0061_auto_20200806_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='value_type',
            field=models.CharField(choices=[('fieldset', 'fieldset'), ('integer', 'integer'), ('decimal', 'decimal'), ('short_string', 'short string'), ('long_string', 'long string'), ('rich_text', 'rich text'), ('rich_text_short', 'short rich text'), ('boolean', 'boolean'), ('date', 'date'), ('user', 'user'), ('geometry', 'geometry'), ('image', 'image'), ('file', 'file'), ('link', 'link'), ('choice', 'choice')], max_length=64, verbose_name='value type'),
        ),
    ]