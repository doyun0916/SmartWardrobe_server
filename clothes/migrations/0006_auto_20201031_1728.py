# Generated by Django 3.1 on 2020-10-31 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0005_auto_20201031_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottomlong',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bottomshort',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dress',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='outerthick',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='outerthin',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='toplong',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='topshort',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
