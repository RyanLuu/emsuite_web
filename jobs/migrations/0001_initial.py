# Generated by Django 3.1.4 on 2021-01-25 20:07

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emap2SecJob',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('name', models.CharField(default='', max_length=300, verbose_name='Job Name')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('time_sub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Submission Time')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0)),
                ('mrc_file', models.FileField(null=True, upload_to='emap2sec', verbose_name='MRC File')),
                ('mrc_filename', models.CharField(default='', max_length=260, verbose_name='MRC Filename')),
                ('contour', models.FloatField(default=0.0, verbose_name='Contour Level')),
                ('sstep', models.PositiveSmallIntegerField(default=2, verbose_name='Stride Step')),
                ('vw', models.PositiveSmallIntegerField(default=5, verbose_name='Sliding Cube Size')),
                ('norm', models.PositiveSmallIntegerField(choices=[(0, 'None'), (1, 'Global'), (2, 'Local')], default=1, verbose_name='Density Normalization')),
            ],
            options={
                'verbose_name': 'Emap2Sec Job',
                'verbose_name_plural': 'Emap2Sec Jobs',
                'db_table': 'emap2sec',
            },
        ),
        migrations.CreateModel(
            name='Emap2SecPlusJob',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('time_sub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Submission Time')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0)),
                ('mrc_file', models.FileField(null=True, upload_to='emap2secplus', verbose_name='MRC File')),
                ('mrc_filename', models.CharField(default='', max_length=260, verbose_name='MRC Filename')),
            ],
            options={
                'verbose_name': 'Emap2Sec+ Job',
                'verbose_name_plural': 'Emap2Sec+ Jobs',
                'db_table': 'emap2sec_plus',
            },
        ),
        migrations.CreateModel(
            name='MainmastJob',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('time_sub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Submission Time')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0)),
                ('mrc_file', models.FileField(null=True, upload_to='mainmast', verbose_name='MRC File')),
                ('mrc_filename', models.CharField(default='', max_length=260, verbose_name='MRC Filename')),
            ],
            options={
                'verbose_name': 'MAINMAST Job',
                'verbose_name_plural': 'MAINMAST Jobs',
                'db_table': 'mainmast',
            },
        ),
        migrations.CreateModel(
            name='MainmastSegJob',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('time_sub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Submission Time')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0)),
                ('mrc_file', models.FileField(null=True, upload_to='mainmastseg', verbose_name='MRC File')),
                ('mrc_filename', models.CharField(default='', max_length=260, verbose_name='MRC Filename')),
            ],
            options={
                'verbose_name': 'MAINMASTseg Job',
                'verbose_name_plural': 'MAINMASTseg Jobs',
                'db_table': 'mainmast_seg',
            },
        ),
    ]
