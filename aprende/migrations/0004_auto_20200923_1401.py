# Generated by Django 3.1.1 on 2020-09-23 20:01

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aprende', '0003_auto_20200923_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='imagen',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
