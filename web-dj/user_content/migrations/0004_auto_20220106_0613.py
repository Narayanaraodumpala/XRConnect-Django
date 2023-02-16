# Generated by Django 3.2.9 on 2022-01-06 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_content', '0003_usercontentmodel_date_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercontentmodel',
            old_name='path',
            new_name='file_path',
        ),
        migrations.RemoveField(
            model_name='usercontentmodel',
            name='content_load_type',
        ),
        migrations.AddField(
            model_name='usercontentmodel',
            name='uploaded_by',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='usercontentmodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usercontentmodel',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterModelTable(
            name='usercontentmodel',
            table='usercontents',
        ),
    ]