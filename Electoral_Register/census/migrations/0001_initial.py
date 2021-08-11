# Generated by Django 3.2.6 on 2021-08-10 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_people', models.CharField(max_length=15)),
                ('place', models.CharField(max_length=15)),
                ('table', models.CharField(max_length=15)),
                ('venc_id', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'people',
            },
        ),
    ]
