# Generated by Django 3.1.2 on 2020-12-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_auto_20201210_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emap2secjob',
            name='norm',
            field=models.PositiveSmallIntegerField(choices=[(0, 'None'), (1, 'Global'), (2, 'Local')], default=0, verbose_name='Density Normalization'),
        ),
        migrations.AlterField(
            model_name='emap2secjob',
            name='sstep',
            field=models.PositiveSmallIntegerField(default=2, verbose_name='Stride Step'),
        ),
        migrations.AlterField(
            model_name='emap2secjob',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0),
        ),
        migrations.AlterField(
            model_name='emap2secjob',
            name='vw',
            field=models.PositiveSmallIntegerField(default=5, verbose_name='Sliding Cube Size'),
        ),
        migrations.AlterField(
            model_name='emap2secplusjob',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0),
        ),
        migrations.AlterField(
            model_name='mainmastjob',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0),
        ),
        migrations.AlterField(
            model_name='mainmastsegjob',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Queued'), (1, 'Running'), (2, 'Completed'), (3, 'Failed')], default=0),
        ),
    ]
