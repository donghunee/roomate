# Generated by Django 2.1.7 on 2019-06-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190602_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='roomate',
            field=models.IntegerField(default=1),
        ),
    ]
