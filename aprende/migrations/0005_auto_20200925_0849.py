# Generated by Django 3.1.1 on 2020-09-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aprende', '0004_auto_20200923_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
