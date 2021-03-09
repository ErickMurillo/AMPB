# Generated by Django 3.1.4 on 2021-03-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=300)),
            ],
            options={
                'verbose_name': 'Área de trabajo',
                'verbose_name_plural': 'Áreas de trabajo',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=300)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Talleres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=300)),
            ],
            options={
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
        ),
        migrations.CreateModel(
            name='TipoEmprendimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=300)),
            ],
            options={
                'verbose_name': 'Tipo de Emprendimiento',
                'verbose_name_plural': 'Tipos de Emprendimientos',
            },
        ),
        migrations.CreateModel(
            name='TipoOrganizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('slug', models.SlugField(editable=False, max_length=300)),
            ],
            options={
                'verbose_name': 'Tipo de organización',
                'verbose_name_plural': 'Tipos de organización',
            },
        ),
    ]