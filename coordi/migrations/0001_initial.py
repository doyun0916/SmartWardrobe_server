# Generated by Django 3.1 on 2020-10-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mancampus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mancasual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mandandy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Manformal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Manminimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mansports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Manstreet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mantravel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wocasual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wofeminine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Woformal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wogirlish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Woromantic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wosports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wostreet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Wotravel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outer', models.CharField(max_length=30)),
                ('outercol', models.CharField(max_length=30)),
                ('top', models.CharField(max_length=30)),
                ('topcol', models.CharField(max_length=30)),
                ('bottom', models.CharField(max_length=30)),
                ('bottomcol', models.CharField(max_length=30)),
                ('imgurl', models.CharField(max_length=30)),
            ],
        ),
    ]
