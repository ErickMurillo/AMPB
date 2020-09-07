# Generated by Django 3.1.1 on 2020-09-02 16:40

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('texto', models.TextField()),
                ('foto', sorl.thumbnail.fields.ImageField(upload_to='banner/')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.AddField(
            model_name='escuela',
            name='foto',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to='escuelas/'),
            preserve_default=False,
        ),
    ]