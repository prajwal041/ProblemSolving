# Generated by Django 2.1.7 on 2019-10-08 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('favcolor', models.CharField(max_length=255)),
                ('pet', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dom',
                'managed': True,
            },
        ),
    ]
