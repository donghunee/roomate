# Generated by Django 2.1.7 on 2019-06-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190605_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='smoke',
            field=models.CharField(default='yes', max_length=10),
        ),
    ]
