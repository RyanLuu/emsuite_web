# Generated by Django 3.1.2 on 2020-12-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20201210_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emap2secjob',
            name='mrc_file',
            field=models.FileField(upload_to='C:\\Users\\ljf\\git\\emsuite_web\\media', verbose_name='MRC File'),
        ),
    ]
