# Generated by Django 2.1.7 on 2019-06-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190602_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kitchen',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='one',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='room',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='room_in',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='shoes',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='sleep',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='thr',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='toilet',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='two',
            field=models.IntegerField(default=1),
        ),
    ]
