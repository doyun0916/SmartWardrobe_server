# Generated by Django 3.1 on 2020-11-18 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0012_auto_20201118_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottomlong',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bottomshort',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dress',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outerthick',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outerthin',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toplong',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topshort',
            name='like',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
