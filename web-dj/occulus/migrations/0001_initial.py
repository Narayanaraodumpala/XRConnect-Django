# Generated by Django 3.2.9 on 2022-04-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oculus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('oculus_id', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'Oculus',
            },
        ),
    ]